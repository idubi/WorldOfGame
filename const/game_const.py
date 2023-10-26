
from games import guess_game,memory_game,currency_roulette_game

AVAILABLE_GAMES = {
    '1': {"game":"Memory Game",             "description": "a sequence of numbers will appear for 1 second and you have to guess it back",  "play" : memory_game.play},
    '2': {"game":"Guess Game",              "description": "guess a number and see if you chose like the computer",                         "play" : guess_game.play},
    '3': {"game":"Currency Roulette",       "description": "try and guess the value of a random amount of USD in ILS",                      "play" : currency_roulette_game.play},
    '4': {"game":"Guess Number Language",   "description": "try and guess the language of a number",                                        "play" : None},
    '5': {"game":"#Number# Boom",           "description": "participate boom game against the computer",                                    "play" : None}
}

