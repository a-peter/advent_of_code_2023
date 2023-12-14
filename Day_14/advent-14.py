from itertools import cycle
import hashlib

file_name = './Day_14/sample-14.1.txt'
file_name = './Day_14/input-advent-14.txt'

platform = [[x for x in line] for line in open(file_name).read().splitlines()]
width = len(platform[0])
height = len(platform)

def move(line_from: list[str], line_to: list[str]) -> int:
    moves = 0
    for x in range(len(line_from)):
        if line_from[x] == 'O' and line_to[x] == '.':
            line_from[x] = '.'
            line_to[x] = 'O'
            moves += 1
    return moves

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

full_cycle = [(tilt_platform, 'N'), (bank_platform, 'W'), (tilt_platform, 'S'), (bank_platform, 'E')]
# full_cycle = 'NWSE'

cycler = cycle(full_cycle)
counter = 0
hashes = []
hash_map = {}
duplicates = []
for c in range(40000):
    for round in range(4):
        direction = next(cycler)
        while direction[0](direction[1]) > 0: pass
        if counter == 0:
            print('Task 1: %d' % caclulate_load()) # 136 / 109638
        counter += 1
        if counter % 4 == 0:
            s = ''.join([''.join(line) for line in platform])
            hex = hashlib.md5(s.encode('utf-8')).hexdigest()
            if hex in hashes:
                print(c, hex, hash_map[hex], sep=' # ')
                loop_start = hash_map[hex][0]
                loop_len = len(hash_map) - loop_start
                no_loop = len(hash_map) - loop_len
                loops = 1_000_000_000 - no_loop
                print(loops, loop_len, loops % loop_len)
                # On first hit we are able to find the loop-size
                # from 1.000.000.000 subtract the non-loop elements
                # and divide the rest by the loop size.
                # Then find the pattern for this step of the loop. -> 2/7/4 for sample | 121/21/18
                index = no_loop + loops % loop_len - 1
                result = [load for i,load in hash_map.values() if i == index][0]
                print('Task 2: %d' % result) # 64 / 102657
                break
                # xxx = caclulate_load()
                # duplicates.append(counter)
                # if len(duplicates) == 3:
                #     loop = duplicates[-1] - duplicates[-2]
                # pass
            else:
                print(c, hex, sep=' - ')
                hash_map[hex] = (c, caclulate_load())
                hashes.append(hex)
    else:
        continue
    break

# done!