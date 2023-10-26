
import os
import requests
import json
 
from random import randint

def Screen_cleaner():
    os.system('clear')     
    
def get_random_value(min,max):
    return randint(min,max)  

def usd_to_ils():
    try:
        url = "https://api.apilayer.com/fixer/convert?to=ILS&from=USD&amount=1"

        payload = {}
        headers = {
            "apikey": "9rSd6tFKuqRLEQg8HJ0dyuDd4JdUXoKO"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        json_object = json.loads(response.text)
        return json_object['info']['rate']
    except:
        print('error trying to get usd to ils conversion rate')
        return False


def is_valid_float(value):
    return value.replace(".",'').isdigit()    

def load_json_file(file_name):
    data=None
    if not os.path.exists(file_name) :
        return data
    try:
        f = open(file_name, "r") 
        data = json.load(f)
        f.close()
    except IOError as e:
        print(f'failed to open file {file_name}  \n ==> (error:  \n {str(e)}  ) ')
    except BaseException as e:
        print (f'failed to read score file data \n ==> (error:  \n {str(e)}  )')
        f.close()
    
    return data


def save_json_file(data, file_name):
    with open(file_name, "w") as f:
        json.dump(data, f)
        f.close()
