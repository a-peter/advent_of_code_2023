from itertools import cycle
import hashlib

file_name = './Day_14/sample-14.1.txt'
file_name = './Day_14/input-advent-14.txt'

platform = [[x for x in line] for line in open(file_name).read().splitlines()]
width = len(platform[0])
height = len(platform)

# moves one row up or down in the platform
def move(line_from: list[str], line_to: list[str]) -> int:
    moves = 0
    for x in range(len(line_from)):
        if line_from[x] == 'O' and line_to[x] == '.':
            line_from[x] = '.'
            line_to[x] = 'O'
            moves += 1
    return moves

# bank does a west or east movement of the platform.
def bank_platform(direction: str) -> int:
    moves = 0
    dir = -1 if direction == 'W' else 1
    r = range(1, width) if direction == 'W' else range(width - 2, -1, -1)
    for row in range(height):
        for x in r:
            if platform[row][x] == 'O' and platform[row][x + dir] == '.':
                platform[row][x] = '.' 
                platform[row][x + dir] = 'O'
                moves += 1
    return moves

# tilt does a north or south movement of the platform.
def tilt_platform(direction: str) -> int:
    moves = 0
    if direction == 'N':
        for r in range(1, len(platform)):
            moves += move(platform[r], platform[r-1])
    else:
        for r in range(0, len(platform) -1):
            moves += move(platform[r], platform[r+1])
    return moves

def caclulate_load() -> int:
    load = 0
    for l, line in enumerate(platform):
        load += line.count('O') * (height - l)
    return load

action_cycle = [(tilt_platform, 'N'), (bank_platform, 'W'), (tilt_platform, 'S'), (bank_platform, 'E')]

cycler = cycle(action_cycle)
hashes = {}
for c in range(40000):
    for round in range(4):
        direction = next(cycler)
        while direction[0](direction[1]) > 0: pass
        if c == 0 and round == 0:
            print('Task 1: %d' % caclulate_load()) # 136 / 109638

    s = ''.join([''.join(line) for line in platform])
    hex = hashlib.md5(s.encode('utf-8')).hexdigest()
    if hex in hashes.keys(): # hashes:
        print(c, hex, hashes[hex], sep=' # ')
        loop_len = len(hashes) - hashes[hex][0]
        no_loop = len(hashes) - loop_len
        loops = 1_000_000_000 - no_loop
        print(loops, loop_len, loops % loop_len)
        # On first hit we are able to find the loop-size
        # from 1.000.000.000 subtract the non-loop elements and modulo this by the loop size.
        # Then find the pattern for this step of the loop. -> 2/7/4 for sample | 121/21/18
        index = no_loop + loops % loop_len - 1
        result = [load for i,load in hashes.values() if i == index][0]
        print('Task 2: %d' % result) # 64 / 102657
        break
    else:
        hashes[hex] = (c, caclulate_load())
        # hashes.append(hex)
        print(c, hex, hashes[hex][1], sep=' - ')

# done!