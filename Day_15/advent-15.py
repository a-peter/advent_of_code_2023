from collections import defaultdict
from functools import cache, reduce
import re

# INPUT = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
INPUT = open('./Day_15/input-advent-15.txt').read().strip()

@cache
def calc_hash(byte_input: str) -> int:
    return reduce(lambda hash, data: ((hash + ord(data)) * 17) % 256, byte_input, 0)

###########################
# Task 1
focusing_power = sum([calc_hash(sequence) for sequence in INPUT.split(',')])
print('Task 1: %d' % focusing_power) # 1320 for sample / 512797 for input

###########################
# Task 2
boxes = defaultdict(dict)
for sequence in INPUT.split(','):
    label, focal_length = re.split(r'[-=]', sequence)
    if focal_length: 
        boxes[calc_hash(label)][label] = int(focal_length)
    else:
        boxes[calc_hash(label)].pop(label, -1)

focusing_power = 0
for slot, lenses in boxes.items():
    for index, focal_length in enumerate(lenses.values(), 1):
        focusing_power += (slot + 1) * index * focal_length

print('Task 2: %d' % focusing_power) # - for HASH / 145 for sample / 262454 for input
