MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def loop_to_get_number(a_string, look_forwards=True):
    if not look_forwards:
        a_string = a_string[::-1]
    for i in a_string:
        try:
            int(i)
            return i
        except ValueError:
            pass        

def loop_to_get_number_part_2(a_string):
    num_indexes = {}
    for num_str in MAP.keys():
        str_index = a_string.find(num_str)
        r_str_index = a_string.rfind(num_str)
        if str_index >= 0:
            num_indexes[str_index] = MAP[num_str]
        if r_str_index >= 0:
            num_indexes[r_str_index] = MAP[num_str]
            
    for i, value in enumerate(a_string):
        try:
            num_indexes[i] = int(value)
        except ValueError:
            pass
    max_value = num_indexes[max(num_indexes.keys())]
    min_value = num_indexes[min(num_indexes.keys())]
    result = str(min_value) + str(max_value)
    return result
    

def get_number_sum(a_string):
    first_number = loop_to_get_number(a_string)
    last_number = loop_to_get_number(a_string, look_forwards=False)
    concat_number = first_number + last_number
    return concat_number

def get_number_sum_part_2(a_string):
    return loop_to_get_number_part_2(a_string)

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_01.txt') as f:
        file_data = f.read()
    lines = file_data.split('\n')
    sums = [get_number_sum(l) for l in lines]
    sums = sum([int(x) for x in sums])
    print(f"Answer to part 1: {sums}")
    
    sums = [get_number_sum_part_2(l) for l in lines]
    sums = sum([int(x) for x in sums])
    print(f"Answer to part 2: {sums}")
