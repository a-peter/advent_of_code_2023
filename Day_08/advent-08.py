import re
from itertools import cycle
from math import lcm

# file_name = './Day_08/sample-08.txt'
# file_name = './Day_08/sample-08.2.txt'
# file_name = './Day_08/sample-08.3.txt'
file_name = './Day_08/input-advent-08.txt'

instructions, _, *str_navigation = open(file_name).read().splitlines()
navigation = {nav[0:3]: (nav[7:10], nav[12:15]) for nav in str_navigation}
starting_nodes = [nav for nav in navigation if nav[-1] == 'A']

iterations = [0] * len(starting_nodes)
for i, pos in enumerate(starting_nodes):
    instruction_cylcer = cycle(int(i == 'R') for i in instructions)
    while pos[-1] == 'Z':
        iterations[i] += 1
        pos = navigation[pos][next(instruction_cylcer)]

print('Task 1: %d steps' % iterations[starting_nodes.index('AAA')]) # should be 19951
print('Task 2: %d steps' % lcm(*iterations)) # should be 16342438708751
