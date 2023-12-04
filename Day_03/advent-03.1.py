numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
adjacent = ['.'] + numbers
offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
array2D = []
max_lines = 0
max_columns = 0
adjacent_numbers = []

def check_adjacent(line, column):
    adjacence = False
    for offset in offsets:
        if 0 <= (line + offset[0]) <= max_lines and 0 <= (column + offset[1]) <= max_columns:
            adjacence |= array2D[line + offset[0]][column + offset[1]] not in adjacent
            
    return adjacence

for line in open('./Day_03/input-advent-03.1.txt'):
# for line in open('./Day_03/sample2.txt'):
    array2D.append(list(line)[0:-1])
    # print(line)

max_lines = len(array2D) - 1
max_columns = len(array2D[0]) -1

is_number, number, is_adjacent = False, 0, False
sum_of_numbers = 0
for line_number, line in enumerate(array2D):
    print(line_number, line)

    if number != 0 and is_adjacent:
        sum_of_numbers += number
        adjacent_numbers.append(number)

    is_number, number, is_adjacent = False, 0, False
    for column, char in enumerate(line):
        if char in numbers:
            is_number = True
            number = int(char) + 10 * number
            is_adjacent |= check_adjacent(line_number, column)
        else:
            if number != 0 and is_adjacent:
                sum_of_numbers += number
                adjacent_numbers.append(number)
            is_number, number, is_adjacent = False, 0, False

print('Sum of numbers with adjacent sign: %d' % sum(adjacent_numbers))
pass