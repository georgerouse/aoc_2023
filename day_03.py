PROCESSED_LOCS = set()

def is_symbol(char):
    return char in ["*", "#", "+", "$", "@", "=", "/", "%", "&", "-"]

def is_adjacent_to_symbol(x, y, grid):
    for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]:
        if 0 <= x + x_offset < len(grid[y]) and \
           0 <= y + y_offset < len(grid):
            if is_symbol(grid[x + x_offset][y + y_offset]):
                return True
    return False

def get_sum_of_part_numbers(grid):
    sum_of_part_numbers = 0
    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if row[j].isdigit() and (i, j) not in PROCESSED_LOCS:
                number, init_j = row[j], j
                while j + 1 < len(row) and row[j + 1].isdigit():
                    number += row[j + 1]
                    j += 1
                
                for y in range(init_j, j + 1):
                    PROCESSED_LOCS.add((i, y))
                    if is_adjacent_to_symbol(i, y, grid):
                        sum_of_part_numbers += int(number)
                        break
            j += 1
        
    return sum_of_part_numbers

if __name__ == "__main__":
    with open("src/moc1/aoc_2023/inputs/day_03.txt") as f:
        file_data = f.read()
    lines = [list(line) for line in file_data.split("\n")]
    total_sum = get_sum_of_part_numbers(lines)
    print(f"Answer to part 1: {total_sum}")
