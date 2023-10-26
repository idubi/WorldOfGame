
 
import time
from utils import Screen_cleaner,get_random_value
from const.global_const import MEMORY_GAME_INTERVAL

 

def generate_sequence(difficulty):
    int_array = []
    while len(int_array) < difficulty :
        num = get_random_value(1, 101)
        if num not in int_array:
            int_array.append(num)
    return int_array

def show_generated_list(array_of_numbers,interval_to_show_items):
    input('press <ENTER> when ready to look at generated items')
    Screen_cleaner()
    for i in array_of_numbers:
        print(i)
        time.sleep(interval_to_show_items)
        Screen_cleaner()

def get_integers_list_from_user(difficulty):
    player_list = input(f' type a list of {difficulty} items just in the right order that was seen \n the list must be separated with comma (,) \n ')
    player_list = player_list.strip("[]").lstrip(",").rstrip(",")
    for i in player_list.split(','):
        if not i.isdigit():
            print(' illegal Values - not all items in list are numbers {player_list}')
            return []
    player_list = [int(i) for i in player_list.split(',')]
    return player_list 
    
    
def compare_lists (generated_list , user_list) :
   comparison_list =  list(map(lambda generate_item, user_item: generate_item - user_item, generated_list, user_list))
   is_equal=True
   for i in range(0,len(comparison_list)):
        if comparison_list[i] > 0:
           is_equal=False
           print (f'the lists are not equal in place {i} ({generated_list[i]} <> {user_list[i]})')
   if is_equal:
        print ('the lists are equal ==>  WIN !!!')
   else:
        print ('the lists are not equal ==>  LOST !!!')
 
   return is_equal

    
def is_list_equal(generated_list , user_list):
    # check that the list size match 
    if len(generated_list) != len(user_list):
        print ('the sizes of the lists does not match {len(generated_list)} <> {len(user_list)} ==> LOST !!!')
        return False
    else:
        return compare_lists(generated_list,user_list)
    
def play(difficulty) :  
    
   generated_sequence = generate_sequence(difficulty)
   show_generated_list(generated_sequence,MEMORY_GAME_INTERVAL)
    
   user_sequence=get_integers_list_from_user(difficulty)
   return is_list_equal(generated_sequence,user_sequence)