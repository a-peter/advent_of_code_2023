import numpy as np
import scipy.ndimage as ndi

#################################
# Read input
file_name = './Day_18/sample-18.1.txt'
file_name = './Day_18/input-advent-18.txt'

dir_to_int = 'RDLU'

dig_plan_1 = []
dig_plan_2 = []
for line in open(file_name).read().splitlines():
    direction, count, col = line.split()
    dig_plan_1.append([dir_to_int.index(direction), int(count)])
    dig_plan_2.append([int(col[-2]), int(col[2:-2], 16)])

# Expected solutions
# Sample:    62 /    952408144115
# Data:   46394 / 201398068194715

# Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
# inner = Area - (boundary/2) + 1
# Shoelace forumla: https://en.wikipedia.org/wiki/Shoelace_formula
# Area = [shoelace]

def make_points(position: tuple[int, int], direction: int, count: int) -> tuple[int, int]:
    if direction == 0: next_position = (position[0] + count, position[1])
    elif direction == 2: next_position = (position[0] - count, position[1])
    elif direction == 1: next_position = (position[0], position[1] + count)
    elif direction == 3: next_position = (position[0], position[1] - count)
    return next_position

def shoelace(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    return 0.5 * abs(sum(x[i]*y[i+1] - x[i+1]*y[i] for i in range(len(points)-1)))

def solve(data: list[tuple[int, int]]) -> int:
    points = [(0, 0)]
    for direction, count in data:
        points.append(make_points(points[-1], direction, count))
    area = shoelace(points)
    boundary_points = sum(line[1] for line in data)
    inner_points = int(area) - boundary_points // 2 + 1
    solution = inner_points + boundary_points
    return solution

print('Task 1: %d' % solve(dig_plan_1))
print('Task 2: %d' % solve(dig_plan_2))
