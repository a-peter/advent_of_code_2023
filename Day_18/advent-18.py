import numpy as np
import scipy.ndimage as ndi

file_name = './Day_18/sample-18.1.txt'
file_name = './Day_18/input-advent-18.txt'

dig_plan = [[line.split()] for line in open(file_name).read().splitlines()]

dir_to_int = 'RDLU'

dig_plan = []
dig_plan_2 = []
for line in open(file_name).read().splitlines():
    direction, count, color = line.split()
    dig_plan.append([direction, dir_to_int.index(direction), int(count), int(color[2:-1], 16)])
    dig_plan_2.append([int(color[-2]), int(color[2:8], 16)])

# [print(line) for line in dig_plan]
# print()

width, height = 1, 1
min_w, min_h = 1_000_000, 1_000_000
max_w, max_h = 0, 0
for line in dig_plan:
    direction, _, count, _ = line # Task 1
    _, direction, count, _ = line # Task 1
    # direction, count = line
    if direction == 0: width += count
    elif direction == 2: width -= count
    elif direction == 1: height += count
    elif direction == 3: height -= count
    max_w, max_h = max(max_w, width), max(max_h, height)
    min_w, min_h = min(min_w, width), min(min_h, height)


print('max WxH: %dx%d' % (max_w, max_h))
print('min WxH: %dx%d' % (min_w, min_h))
print()


position = (-min_w + 1, -min_h + 1)
max_w = max_w - min_w + 1
max_h = max_h - min_h + 1

print('max WxH: %dx%d' % (max_w, max_h))
print('Start: %d,%d' % (position[0], position[1]))

loop = np.array([np.array([0 for x in range(max_w)]) for y in range(max_h)])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# position = [0, 0] # x,y
loop[position[1], position[0]] = 1
for instruction in dig_plan:
    for i in range(instruction[2]):
        position = (position[0] + directions[instruction[1]][0], position[1] + directions[instruction[1]][1])
        loop[position[1], position[0]] = 1

[print(''.join(['#' if x else '.' for x in line])) for line in loop]
print()

filled_loop = ndi.binary_fill_holes(loop)

[print(''.join(['#' if x else '.' for x in line])) for line in filled_loop]
print()

volume = sum(sum([line for line in filled_loop]))
print('Task 1: %d m²' % volume) # ? / 46394