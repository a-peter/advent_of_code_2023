import re

# file_name = './Day_08/sample-08.txt'
# file_name = './Day_08/sample-08.2.txt'
file_name = './Day_08/sample-08.3.txt'
# file_name = './Day_08/input-advent-08.txt'

def next_instruction(instruction_index):
    instruction = int(instructions[instruction_index] == 'R')
    instruction_index = (instruction_index + 1) % len(instructions)
    return (instruction, instruction_index)

regex = re.compile('(\w+) = \((\w+), (\w+)\)')
navigation = dict()
for i, line in enumerate(open(file_name)):
    if i == 0:
        instructions = line.strip()
    elif i >= 2:
        match = regex.search(line)
        navigation[match.group(1)] = (match.group(2), match.group(3))

location, end = 'AAA', 'ZZZ'
instruction_index = 0
steps = 0
while True:
    instruction, instruction_index = next_instruction(instruction_index)
    location, steps = (navigation[location][instruction], steps + 1)
    if location == end:
        break
# should be 19951 for input-advent-08.txt

print('Task 1: %d steps' % steps)
