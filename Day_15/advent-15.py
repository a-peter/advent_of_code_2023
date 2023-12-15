import functools
import re

file_name = './Day_15/input-advent-15.txt'

INPUT = 'HASH'
INPUT = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
INPUT = open(file_name).read().strip()


@functools.cache
def calc_hash(byte_input: bytes) -> int:
    hash = 0
    for c in byte_input:
        hash = ((hash + c) * 17 ) % 256
    return hash

sum = 0
for sequence in INPUT.split(','):
    input_bytes = sequence.encode('utf-8')
    sum += calc_hash(input_bytes)

print('Task 1: %d' % sum) # 52 for HASH / 1320 for sample / 512797 for input

###########################
# Task 2

def find(label: str, lenses: []) -> int:
    for i,(lens,_) in enumerate(lenses):
        if lens == label:
            return i
    return -1

map = {i:[] for i in range(256)}
for sequence in INPUT.split(','):
    label, focus = re.split(r'[-=]', sequence)
    box_number = calc_hash(label.encode('utf-8'))
    # print(label, box_number)
    lens_index = find(label, map[box_number])
    if len(focus) > 0: # xxx=7
        if lens_index == -1:
            map[box_number].append( (label, int(focus)) )
        else:
            map[box_number][lens_index] = (label, int(focus))
            pass
    else: # xxx-
        if lens_index != -1: 
            lenses = map[box_number]
            map[box_number] = lenses[:lens_index] + lenses[lens_index + 1:]
    pass

# Focusing power
sum = 0
for slot in map.keys():
    for index, (_, focus) in enumerate(map[slot]):
        sum += (slot + 1) * (index + 1) * focus
        pass

print('Task 2: %d' % sum) # - for HASH / 145 for sample / 262454 for input
