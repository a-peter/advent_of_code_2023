from functools import reduce
import math

def calc_solution(time, distance):
    solution1 = (time/2) + math.sqrt((time * time)/4 - distance)
    solution2 = (time/2) - math.sqrt((time * time)/4 - distance)

    # Special case: the zeroes are without decimals
    if math.floor(solution1) == solution1:
        solution1 -= 1
    if math.ceil(solution2) == solution2:
        solution2 += 1

    result = math.floor(solution1) - math.ceil(solution2) + 1
    return result

#####################
# Read input
input = []
input2 = []

for line in open('./Day_06/input-advent-06.1.txt'):
# for line in open('./Day_06/sample-06.1.txt'):
    input.append([int(i) for i in line[line.index(':') + 1:].split()])
    input2.append(int(line[line.index(':') + 1:-1].replace(' ', '')))

#####################
# Task 2

task_1 = 1
for race in range(len(input[0])):
    task_1 *= calc_solution(input[0][race], input[1][race])

print('Task 1: %d mm' % task_1)
# should be 219849

#####################
# Task 2

print('Task 2: %d mm' % calc_solution(input2[0], input2[1]))
# should be 29432455
