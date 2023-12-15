file_name = './Day_15/input-advent-15.txt'

INPUT = 'HASH'
INPUT = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
# INPUT = open(file_name).read().strip()

sum = 0
for sequence in INPUT.split(','):
    input_bytes = sequence.encode('utf-8')
    hash = 0
    for c in input_bytes:
        hash = ((hash + c) * 17 ) % 256
    sum += hash
    # print(sequence, hash)

print('Task 1: %d' % sum) # 52 for HASH / 1320 for sample / 512797 for input
