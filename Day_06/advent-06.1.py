from functools import reduce
import math

# The formula to be done is a quadratic formula:
# x * (time - x) = distance
# -x² + time*x - distance = 0
# Just find the solutions for this quadratic formula. Take
# the correctly rounded inner int solutions.
# Special case for the sample data: The solutions *are* int.
# For my data the special case wasn't necessary.

def calc_solution(time, distance):
    sqrt = math.sqrt((time * time)/4 - distance)
    solution_lower = (time/2) - sqrt # lower limit
    solution_upper = (time/2) + sqrt # upper limit

    result = (math.ceil(solution_upper) - 1) - (math.floor(solution_lower) + 1) + 1
    return result

#####################
# Read input
input = []

for line in open('./Day_06/input-advent-06.1.txt'):
# for line in open('./Day_06/sample-06.1.txt'):
    input.append([int(i) for i in line.split()[1:]])
    
#####################
# Task 1
task_1 = 1
for race in range(len(input[0])):
    task_1 *= calc_solution(input[0][race], input[1][race])

print('Task 1: %d mm' % task_1)
# should be 219849
# 288 for sample

#####################
# Task 2
time, dist = [int(''.join(l.split()[1:])) for l in open('./Day_06/input-advent-06.1.txt')]
print('Task 2: %d mm' % calc_solution(time, dist))
# should be 29432455
