import re
import code

def extract_game_number(game_data):
    pattern = r'Game (\d{1,}):'
    match = re.search(pattern, game_data)
    return match.group(1)

def replace_game_text(game_data):
    pattern = r'Game (\d{1,}):'
    clean_game_data = re.sub(pattern, '', game_data)
    return clean_game_data

def split_rounds(game_data):
    rounds = game_data.split(';')
    return rounds

def extract_color_quantity(round_data, color):
    colors = ['red','green','blue']
    pattern = rf'(\d{{1,}}) {color}'
    match = re.search(pattern, round_data)
    if match:
        return match.group(1)
    else:
        return '0'

def read_file_contents(file_path):
    games = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip newline characters and add to the list
            games.append(line.strip())
    return games

colors = ['red','green','blue']

games_data = read_file_contents('input.txt')
parsed_games_data = []

for game in games_data:
    game_number = extract_game_number(game)
    clean_game_data = replace_game_text(game)
    rounds = split_rounds(clean_game_data)
    game_template = {"game_number": game_number,"rounds": [], "max_values": {color: 0 for color in colors}}

    for index, round in enumerate(rounds,1):
        round_number = str(index)
        round_dict = {}
        for color in colors:
            quantity = extract_color_quantity(round,color)
            round_dict[color] = quantity
            game_template["max_values"][color] = max(game_template["max_values"][color], int(quantity))
            # code.interact(local=locals())
            game_template["rounds"].append(round_dict)

    parsed_games_data.append(game_template)

# Answers part 1
valid_game_numbers = []
for game in parsed_games_data:
    red_valid = game['max_values']['red'] <= 12
    green_valid = game['max_values']['green'] <= 13
    blue_valid = game['max_values']['blue'] <= 14
    if red_valid and green_valid and blue_valid:
        valid_game_numbers.append(int(game['game_number']))

print(sum(valid_game_numbers))

# Answers part 2
game_powers = []
for game in parsed_games_data:
    game_power = game['max_values']['red'] * game['max_values']['green'] * game['max_values']['blue']
    game_powers.append(game_power)

print(sum(game_powers))

