import re
from itertools import cycle
from math import lcm

# file_name = './Day_08/sample-08.txt'
# file_name = './Day_08/sample-08.2.txt'
# file_name = './Day_08/sample-08.3.txt'
file_name = './Day_08/input-advent-08.txt'

# def next_instruction(instruction_index):
#     instruction = int(instructions[instruction_index] == 'R')
#     instruction_index = (instruction_index + 1) % len(instructions)
#     return (instruction, instruction_index)

regex = re.compile('(\w+) = \((\w+), (\w+)\)')
navigation = dict()
starting_nodes = []
for i, line in enumerate(open(file_name)):
    if i == 0:
        instructions = line.strip()
    elif i >= 2:
        match = regex.search(line)
        navigation[match.group(1)] = (match.group(2), match.group(3))
        if match.group(1).endswith('A'):
            starting_nodes.append(match.group(1))


# Task 1
# location, end = 'AAA', 'ZZZ'
# instruction_index = 0
# steps = 0
# while True:
#     instruction, instruction_index = next_instruction(instruction_index)
#     location, steps = (navigation[location][instruction], steps + 1)
#     if location == end:
#         break
# print('Task 1: %d steps' % steps)
# should be 19951 for input-advent-08.txt

# Task 2
instruction_index = 0
steps = 0

instruction_cylcer = cycle(int(i == 'R') for i in instructions)
iterations = []
for i, pos in enumerate(starting_nodes):
    steps = 0
    instruction_cylcer = cycle(int(i == 'R') for i in instructions)
    while not pos[-1] == 'Z':
        steps += 1
        pos = navigation[pos][next(instruction_cylcer)]
    iterations.append(steps)

print('Task 1: %d steps' % iterations[starting_nodes.index('AAA')])
print('Task 2: %d steps' % lcm(*iterations))

last_step = 0
while True:
    instruction = next(instruction_cylcer)

    # all_finished = True
    # for i, node in enumerate(starting_nodes):
    #     starting_nodes[i] = navigation[starting_nodes[i]][instruction]
    #     all_finished = all_finished and starting_nodes[i][-1] == 'Z'

    all_finished = False #True
    i = 6
    starting_nodes[i] = navigation[starting_nodes[i]][instruction]
    if starting_nodes[i][-1] == 'Z':
        print(steps, steps - last_step)
        last_step = steps
        # starting_nodes[i] = navigation[node][instruction]
        # all_finished = all_finished and starting_nodes[i][-1] == 'Z'

    steps += 1
    if all_finished:
        break

print('Task 1: %d steps' % steps)
