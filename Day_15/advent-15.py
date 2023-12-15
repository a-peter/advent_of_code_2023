from collections import defaultdict
import functools
import re

# Optimized, thanks to https://github.com/SteffenHaeussler/advent_of_code/blob/main/day_15/day_15.ipynb

file_name = './Day_15/input-advent-15.txt'

INPUT = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
INPUT = open(file_name).read().strip()

@functools.cache
def calc_hash(byte_input: bytes) -> int:
    return functools.reduce(lambda hash, data: ((hash + data) * 17) % 256, byte_input, 0)

###########################
# Task 1
focusing_power = sum([calc_hash(sequence.encode('utf-8')) for sequence in INPUT.split(',')])
print('Task 1: %d' % focusing_power) # 1320 for sample / 512797 for input

###########################
# Task 2
boxes = defaultdict(dict)
for sequence in INPUT.split(','):
    label, focal_length = re.split(r'[-=]', sequence)
    box_number = calc_hash(label.encode('utf-8'))

    if focal_length: 
        boxes[box_number][label] = int(focal_length)
    else:
        boxes[box_number].pop(label, -1)

focusing_power = 0
for slot, lenses in boxes.items():
    for index, focal_length in enumerate(lenses.values(), 1):
        focusing_power += (slot + 1) * index * focal_length

print('Task 2: %d' % focusing_power) # - for HASH / 145 for sample / 262454 for input
