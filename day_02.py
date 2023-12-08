import re
from typing import List

class GameSet:
    def __init__(self, blue_count, green_count, red_count) -> None:
        self.blue_count = blue_count
        self.green_count = green_count
        self.red_count = red_count
        
class Game:
    def __init__(self, game_number, set_obj_list) -> None:
        self.game_number = game_number
        self.set_obj_list = set_obj_list

def split_cube_info(cubes, colour):
    if colour not in cubes:
        return 0
    else:
        num_regex = r"[0-9]*"
        colour_num = re.match(num_regex, cubes)
        return int(colour_num.group(0))

def parse_set_string(set_string):
    cubes = set_string.split(", ")
    red_count_total = 0
    green_count_total = 0
    blue_count_total = 0
    for cube_count in cubes:
        red_count_total += split_cube_info(cube_count, "red")
        green_count_total += split_cube_info(cube_count, "green")
        blue_count_total += split_cube_info(cube_count, "blue")
    return GameSet(blue_count_total, green_count_total, red_count_total)

def parse_file_row(line):
    game_num = None 
    game_regex = r"Game [0-9]*: "
    game_num_search = re.search(game_regex, line)
    game_num_string = line[game_num_search.span()[0]:game_num_search.span()[1]]
    game_num = int(re.findall(r"\d+", game_num_string)[0])
    sets_info = line[game_num_search.span()[1]:]
    set_list = sets_info.split("; ")
    game_sets = [parse_set_string(x) for x in set_list]
    return game_num,  game_sets 

def determine_possible_games(target_game_set, game_list):
    list_of_valid_games = []
    for game in game_list:
        valid = True
        game_number = game.game_number
        for game_set in game.set_obj_list:
            if game_set.green_count > target_game_set.green_count:
                valid = False
            elif game_set.red_count > target_game_set.red_count:
                valid = False
            elif game_set.blue_count > target_game_set.blue_count:
                valid = False
                
        if valid:
            list_of_valid_games.append(game_number)
        
    return list_of_valid_games

def get_power(game_obj):
    min_red = 0
    min_green = 0
    min_blue = 0
    set_obj_list = game_obj.set_obj_list
    for set_obj in set_obj_list:
        if set_obj.green_count > min_green:
            min_green = set_obj.green_count
        if set_obj.red_count > min_red:
            min_red = set_obj.red_count
        if set_obj.blue_count > min_blue:
            min_blue = set_obj.blue_count
    return min_red * min_green * min_blue

if __name__ == "__main__":
    # Get the input data
    with open("inputs/day_02.txt") as f:
        file_data = f.read()
    lines = file_data.split("\n")
    game_list = []
    for line in lines:
        game_num, game_sets = parse_file_row(line)
        game_list.append(Game(game_num, game_sets))
    target_game_set = GameSet(blue_count=14, green_count=13, red_count=12)
    possible_games = determine_possible_games(target_game_set, game_list)
    print(f"Answer to part 1: {sum(possible_games)}")
    
    power_list = [get_power(x) for x in game_list]
    print(f"Answer to part 2: {sum(power_list)}")
