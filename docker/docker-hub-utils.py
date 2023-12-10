import sys
import requests
import json
import subprocess

   
DOCKER_ENDPOINTS = {
    'API_URL' : 'https://hub.docker.com/v2/',
    'LOGIN' : 'users/login'     ,
    'REPO_TAGS' : 'namespaces/{user}/repositories/{repo_name}/tags',
    'REPO_DELETE_TAG' : 'repositories/{user}/{repo_name}/tags/{tag_name}'
}

DOCKER_RESPONSE = {
    'TOKEN':''      
}

# Buld format : VESION.RELEASE.BUILD
BUILD_POSITION_4INCREMENTAL_TYPES = {
    "VERSION":0,
    "RELEASE" : 1,
    "BUILD": 2    
}

def get_docker_login_url() : 
    return DOCKER_ENDPOINTS['API_URL'] + DOCKER_ENDPOINTS['LOGIN']  
def get_docker_repo_url(user,repo_name):
    str = DOCKER_ENDPOINTS["API_URL"] + DOCKER_ENDPOINTS["REPO_TAGS"]  
    return str.replace('{user}',user).replace('{repo_name}',repo_name)
def get_docker_delete_tag_url(user,repo_name,tag_name):
    str = DOCKER_ENDPOINTS["API_URL"] + DOCKER_ENDPOINTS["REPO_DELETE_TAG"]  
    return str.replace('{user}',user).replace('{repo_name}',repo_name).replace('{tag_name}',tag_name)


def get_latest_build_tag(tags_object):
    return max(tags_object, key=lambda x: int(x['tag_name'].replace('.','')))['tag_name']

def increase_build_tag(current_buildnumber,incremental_type):
    build_number_array = current_buildnumber[::1].split('.')
    new_type_value = int(build_number_array[BUILD_POSITION_4INCREMENTAL_TYPES[incremental_type]])+1
    build_number_array[BUILD_POSITION_4INCREMENTAL_TYPES[incremental_type]]=str(new_type_value)
    array_iteration_calculation = len(BUILD_POSITION_4INCREMENTAL_TYPES)-BUILD_POSITION_4INCREMENTAL_TYPES[incremental_type]
    for i in range(array_iteration_calculation-1):
        build_number_array[len(build_number_array) - i - 1 ]='0'
        
    # next_buildnumber = f'{build_number_array[2]}.{build_number_array[1]}.{build_number_array[0]}'
    next_buildnumber = ".".join(build_number_array)
    print (f' {incremental_type} number increaed from {current_buildnumber} to {next_buildnumber}')
    return  next_buildnumber

def get_header_with_token(token)  : 
    return { 'Accept': 'application/json',
             'Authorization': 'Bearer ' + token}
    
def api_login(user,password):
    url = get_docker_login_url()
    payload = json.dumps({
        "username": user,
        "password": password
        })
    headers = {
         'Content-Type': 'application/json'
         }    
    return requests.request("POST", url=url,headers=headers,data=payload)

def api_get_repo_list(repo_name, user,token):
        url = get_docker_repo_url(user,repo_name)
        headers = get_header_with_token(token) 
        response = requests.request("GET", url=url, headers=headers, data={})
        return response

def api_delete_tag_name(user,repo_name,token,tag_name):
        url = get_docker_delete_tag_url(user,repo_name,tag_name)
        headers = get_header_with_token(token) 
        response = requests.request("DELETE", url=url, headers=headers, data={})
        return response
            
    
def login_to_docker(password,user): 
    try :
        response = api_login( password=password,user=user)
        
        if response.status_code == 200:
            DOCKER_RESPONSE['TOKEN'] = response.json()['token']
            print('success !!! connected to docker hub') 
            return True
        else:
            print(f'faile to login to docker hub , status : {response.status_code} , {response["detail"]}')
            return False
    except Exception as E:
        print (f'failed to login to docker hub ({type(E)} \n {E.args}) \n {E} ')
        return False

def get_repo_tags_json(repo_name , user)  :
     token = DOCKER_RESPONSE["TOKEN"]
     if (token):
        response = api_get_repo_list(repo_name , user , token)
        return response.json()
     else:
        print('error : docker response [TOKEN] have no value')  
        return {}
      
def parse_json_to_tags_list(repo_json):
    result_list = [
    {
        "id": item["id"],
        "push_date": item["tag_last_pushed"],
        "last_pulled": item["tag_last_pulled"],
        "tag_name":item["name"]
    }
    for item in repo_json["results"]
    ]
    return  result_list

def evaluate_tag_name(tag_name) : 
    tag_elements = tag_name.split('.')
    tag_elements.reverse() 
    value = sum(int(element) * 10 ** i for i, element in enumerate(tag_elements))
    # print(f'evaluating {tag_name} ==> {value}')
    return value
    

def get_list_of_tags_to_delete(repository_tags,number_builds_2keeep):
    if len(repository_tags) < number_builds_2keeep - 1 :
        return []
    else :
        sorted_list = sorted(repository_tags, key=lambda x: evaluate_tag_name(x['tag_name']))
        return sorted_list[:len(repository_tags)-number_builds_2keeep]
    

def get_next_tagname_and_tags_2delete(repository_tags,build_incremental_type,number_builds_2keep):
    max_tag_name = get_latest_build_tag(repository_tags) 
    next_tag_name = increase_build_tag(max_tag_name,build_incremental_type)
    tags_to_delete = get_list_of_tags_to_delete(repository_tags,number_builds_2keep)
    return {"next_tag_name" : next_tag_name , "tags_to_delete":tags_to_delete}    

def create_docker_image_tag_for_push(user,repo_name,tag) :
    tag_name = f'{user}/{repo_name}:{tag}'
    try:
        subprocess.run (f'docker tag {repo_name} {tag_name}',shell=True,capture_output=True,text=True,check=True)
        pushed_image = subprocess.run (f'docker push {tag_name}',shell=True,capture_output=True)
        if pushed_image.returncode == 0:
            print(f'{tag_name} was pushed to repository {user}/{repo_name}')
            return True
        else: 
            print (f'failed to push {tag_name} , error is {pushed_image.stderr.decode()}')
            return False
    except:
        return False
    

    
def delete_old_images(user,repo_name,control_obj):
    tags_to_delete = control_obj["tags_to_delete"]
    token = DOCKER_RESPONSE["TOKEN"]
    failed_list = []
    for tag_reference in tags_to_delete:
       tag_name = tag_reference['tag_name']
       print (f'deleting old build : {tag_name} ')
       response = api_delete_tag_name(user,repo_name,token,tag_name)
       if response.status_code!=204:
           failed_list.push({"tag_name":f'{tag_name}',"status_code":f'response.status_code' , "reason":f'{response.reason}'})
       else: 
           print (f'{tag_name} deleted successfuly ')
           
    if failed_list:
        print (f'faile to delete old builds, details :  \n {failed_list}')
        return False
    else :
        return True
       
    

def build_docker_container(repo_name , user , password,build_incremental_type,number_builds_2keep) : 
    if login_to_docker(user=user,password=password):    
        repository_obj = get_repo_tags_json(repo_name,user)
        repository_tags_obj = parse_json_to_tags_list(repository_obj)
        control_obj = get_next_tagname_and_tags_2delete(repository_tags_obj,build_incremental_type,int(number_builds_2keep))
        if create_docker_image_tag_for_push(user,repo_name,control_obj["next_tag_name"]):
            return delete_old_images(user,repo_name,control_obj) 
        else:
            return False 
    else:
        return False

 
# if build_docker_container(user="idubi", password="dckr_pat_qf2cugkVszRwfktFzibi7Su6jD0" , repo_name="world-of-games"):
#     print (f'{DOCKER_RESPONSE}')
    
# build_docker_container(user="idubi", password="dckr_pat_qf2cugkVszRwfktFzibi7Su6jD0" , 
#                         repo_name="world-of-games",
#                         build_incremental_type="RELEASE",
#                         number_builds_2keep=5)


# increase_build_tag("35.0.1","VERSION")
# increase_build_tag("3.40.0","VERSION")
# increase_build_tag("10.4.0","VERSION")
# increase_build_tag("3.0.0","VERSION")
# increase_build_tag("0.10.9","RELEASE")
# increase_build_tag("2.10.9","RELEASE")
# increase_build_tag("0.4.5","RELEASE")
# increase_build_tag("0.0.0","BUILD")
# increase_build_tag("0.0.9","BUILD")
# increase_build_tag("0.10.10","BUILD")


    
# build_docker_container(user="idubi", password="dckr_pat_qf2cugkVszRwfktFzibi7Su6jD0" , 
#                         repo_name="world-of-games",
#                         build_incremental_type="RELEASE",
#                         number_builds_2keep=1)
arg = sys.argv

build_docker_container(user=arg[1] , password=arg[2] , repo_name=arg[3] , build_incremental_type=arg[4], number_builds_2keep=arg[5])