

from utils import usd_to_ils,get_random_value,is_valid_float
from const.global_const import CURRENCY_ROULETTE_DIVERSION
 


def get_money_interval(difficulty , total):
       return {"min":total- CURRENCY_ROULETTE_DIVERSION + difficulty , "max":total + CURRENCY_ROULETTE_DIVERSION - difficulty}

def get_guess_from_user(total) :
       val = 0
       while not val:
              val = input (f'please type the Israeli value of {total} USD($) : ')
              if not is_valid_float(val):
                     val=0;  
                     print (f'please type valid amount of mony (float or integer) in Israeli shekels')
       return float(val)
 
def compare_guess_to_interval(user_guess,interval,usd_rate,total_money):
       # print (f'user_guess   : {user_guess}  \n interval     : {interval } max={interval.get("max")*usd_rate}   , min={interval.get("min")*usd_rate} \n usd_rate     : {usd_rate}   \n total_money  : {total_money}'  )
       if (user_guess <= interval.get('max')*usd_rate  and 
           user_guess >= interval.get('min')*usd_rate ):
          print ('you WON the CURRENCY ROULETTE game  !!! ==> WIN !!! ')
          return True
       print (f'you FAILED to calculate the total requested mony {total_money} in USD , in the given interval {interval}  !!! ')
       return False 
          
      
    
def play(difficulty) :      
   usd_rate = usd_to_ils()
   if not usd_rate:
      print(f'failed to get usd rate, game is disabled')
      return True
   total_money = get_random_value(0,100)
   interval = get_money_interval(difficulty,total_money)
   user_guess = get_guess_from_user(total_money)
   return compare_guess_to_interval(user_guess,interval,usd_rate,total_money)
   
   
