from const.game_const import AVAILABLE_GAMES


def get_game_selections(games_dictionary):
    games_message = 'Please choose a game to play: \n'
    for game_id in games_dictionary:
        games_message = games_message + f'({game_id})  {games_dictionary.get(game_id).get("game")}  -  {games_dictionary.get(game_id).get("description")} . \n'
    return games_message


def validate_game_difficulty():
    selection = input("please select a game difficulty (1 .. 5) \n")
    if not selection.isdigit() :
        print('selected value must be number')
        return False
    selection = int(selection)
    if selection < 1 or selection > 5:
        print('difficulty out of range')
        return False
    else:
        return selection


def validate_game_selection():
    selection = input("please select game number from list \n")
    if AVAILABLE_GAMES.get(selection):
        return selection
    else:
        print('selected value not valid')
        return False


def get_welcome_message(name):
    return f'Hello {name} and welcome to the World of Games (WoG). ' \
           f'\nHere you can find many cool games to play.\n\n'


def print_user_selection(input):
    print(input)


def welcome(input):
    print(get_welcome_message(input.get('user_name')))
    if load_game(input):
        print(f' \n  \n user selection summery: \n {input} ')



def load_game(input):
    print(get_game_selections(AVAILABLE_GAMES))
    while not input['selected_game']:
        input['selected_game'] = validate_game_selection()
    while not input['game_difficulty']:
        input['game_difficulty'] = validate_game_difficulty()
    return True


def play_game(input):
    play = AVAILABLE_GAMES.get(input.get("selected_game")).get("play")
    if (play):
        return play(input.get("game_difficulty"))        
    else :
        print(f'Game {AVAILABLE_GAMES.get(input.get("selected_game")).get("game")}' \
            ' is not initialized \n (for demonstration purposes , ' \
            'you will get full point on it). \n '\
            'on production no points will be received')
        return True