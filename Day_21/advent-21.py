import functools
import numpy as np

file_name, step_count = './Day_21/sample-21.1.txt', 50
# file_name, step_count = './Day_21/input-21.txt', 64

# Read and prepare data
map = [line for line in open(file_name).read().splitlines()]
start = [(i, line.index('S')) for i,line in enumerate(map) if 'S' in line][0]

map_width, map_height = (len(map[0]), len(map))

# [print(line) for line in map]
# print(start)

# Adds two tuples
@functools.cache
def add_tuples(move, position) -> tuple[int, int]:
    return (move[0] + position[0], move[1] + position[1])

@functools.cache
def normalize(position: tuple[int, int]) -> tuple[int, int]:
    return ( (position[0] + map_width) % map_width, (position[1] + map_height) % map_height )

# Tests if move to new position is possible
@functools.cache
def try_move(move: tuple[int, int]) -> tuple[int, int]:
    move_norm = normalize(move)
    if map[move_norm[1]][move_norm[0]] in '.S':
        return move
    return None

# Algorithm
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)] # possible moves
positions = [start]
for i in range(step_count):
    new_positions = []
    for position in positions:
        pass
        for move in moves:
            if new := try_move(add_tuples(move, position)):
                if not new in new_positions:
                    new_positions.append(new)
    positions = new_positions

# Output of result
# for (x,y) in positions:
#     map[y] = map[y][:x] + 'O' + map[y][x+1:]
# [print(line) for line in map]

print('Task 1: %d plots' % len(positions))