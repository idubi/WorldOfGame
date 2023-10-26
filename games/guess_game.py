
from utils import get_random_value
 

def generate_number(difficulty):
    return get_random_value(1,difficulty)

def get_guess_from_user(difficulty):
    num = input(f'please type a number between 1 and {difficulty} :')
    if num.isdigit():
        return int(num)
    else:
        print('input number is not valid , please type in a real number')
        return 0
    
def compare_results(secret , guess) :
     
    print (f'generated : {secret} , guessed : {guess} ==> {"WIN !!!" if secret==guess else "LOST !!!"}')
    return secret == guess
    
def play(difficulty) :     
   secret_number= generated_number = generate_number(difficulty)
   guessed_number = 0
   while not guessed_number:
         guessed_number = get_guess_from_user(difficulty)
   return compare_results(secret_number,guessed_number)
        