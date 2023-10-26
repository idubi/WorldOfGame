from game_control import welcome,play_game
from const.global_const import user_input
from utils import Screen_cleaner
from score import get_user_score,save_user_score,add_score
 



   
Screen_cleaner()
user_input['user_name'] = str(input('please enter your name \n'))
welcome(user_input)
Screen_cleaner()
if play_game(user_input) :
    score = add_score(user_input['game_difficulty'],user_input['user_name'])

 