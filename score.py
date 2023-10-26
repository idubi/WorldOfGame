from utils import load_json_file,save_json_file
from const import global_const

ALL_USERS_SCORES = load_json_file(global_const.SCORES_FILE_NAME)


def get_score_file_name():
    return global_const.SCORES_FILE_NAME

def get_user_score(user_name):
    # data = ALL_USERS_SCORES
    # I want to load this all of the time from fle , since I want tokeep track of gameplay in main process 
    # thw othe solution will be to update this score with rest api from main 
    data = load_json_file(get_score_file_name())
    score = -1 
    if data :
        if user_name:
            score = data.get(user_name) or 0
        else :
            return data         
    return score # if return -1 mwaning that he data is mising at all , not just user  ==> error to rest api

# need to add user score to file json
#    - if file exist get current json 
#    - replace it if exists or add it to json
#    - save file with new json (override)

def save_user_score(user_name,score):
    #data = load_json_file(get_score_file_name())
    data = ALL_USERS_SCORES
    if data :
        data[user_name]=score
    else :
        data = {user_name:score}
    save_json_file(data,get_score_file_name())
    if ALL_USERS_SCORES : 
          ALL_USERS_SCORES[user_name]=score

    
    
    
        

def get_score(difficulty) : 
    return  difficulty * 3 + 5


def add_score(difficulty,user_name):
    POINTS_OF_WINNING = get_score(difficulty)
    USER_TOTAL_SCORE=get_user_score(user_name)
    user_score=USER_TOTAL_SCORE+POINTS_OF_WINNING
    save_user_score(user_name,user_score)
    return user_score
