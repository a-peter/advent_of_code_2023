from collections import defaultdict

signs_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs_gears = ['*']
offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
array2D = []
max_lines = 0
max_columns = 0

def check_gear_sign(line, column):
    gears = set()
    for offset in offsets:
        if 0 <= (line + offset[0]) <= max_lines and 0 <= (column + offset[1]) <= max_columns:
            if array2D[line + offset[0]][column + offset[1]] in signs_gears:
                gears.add((line + offset[0], column + offset[1]))
    return gears

for line in open('./Day_03/input-advent-03.1.txt'):
    array2D.append(list(line)[0:-1])

max_lines = len(array2D) - 1
max_columns = len(array2D[0]) -1

is_number, number, gears_for_number = False, 0, set()
gears = defaultdict(list)

for line_number, line in enumerate(array2D):
    # print(line_number, line)

    if number != 0 and len(gears_for_number) > 0:
        for gear in gears_for_number:
            gears[gear].append(number)
        is_number, number, gears_for_number = False, 0, set()

    is_number, number = False, 0
    for column, char in enumerate(line):
        if char in signs_numbers:
            is_number = True
            number = int(char) + 10 * number
            adjacent_gears = check_gear_sign(line_number, column)
            gears_for_number = gears_for_number.union(adjacent_gears)
        else:
            if number != 0 and len(gears_for_number) > 0:
                for gear in gears_for_number:
                    gears[gear].append(number)
            is_number, number, gears_for_number = False, 0, set()

sum_of_numbers = 0
for gear in gears.keys():
    if len(gears[gear]) > 1:
        sum_of_numbers += gears[gear][0] * gears[gear][1]

print('Sum of gears: %d' % sum_of_numbers)
pass