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

def two_steps(positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    for i in range(2):
        new_positions = set()
        for position in positions:
            pass
            for move in moves:
                if new := try_move(add_tuples(move, position)):
                    new_positions.add(new)
        positions = list(new_positions)
                
    return positions

# Algorithm
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)] # possible moves
positions = [start]

# if number of steps uneven -> make one step.
if step_count % 2 == 1:
    positions = two_steps(positions)
    step_count -= 1

solutions = positions
for i in range(step_count // 2):
    positions = two_steps(positions)
    new_positions = []
    for position in positions:
        if not position in solutions:
            solutions.append(position)
            new_positions.append(position)
    positions = new_positions


# Output of result
# for (x,y) in positions:
#     map[y] = map[y][:x] + 'O' + map[y][x+1:]
# [print(line) for line in map]

# print('Task 1: %d plots' % len(positions))
print('Task 1: %d plots' % len(solutions))