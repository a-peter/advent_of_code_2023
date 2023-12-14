file_name = './Day_14/sample-14.1.txt'
file_name = './Day_14/input-advent-14.txt'

platform = [[x for x in line] for line in open(file_name).read().splitlines()]

def move(line_from: list[str], line_to: list[str]) -> int:
    moves = 0
    for x in range(len(line_from)):
        if line_from[x] == 'O' and line_to[x] == '.':
            line_from[x] = '.'
            line_to[x] = 'O'
            moves += 1
    return moves


def tilt_platform() -> int:
    moves = 0
    for r in range(1, len(platform)):
        for x in range(len(platform[0])):
            moves += move(platform[r], platform[r-1])
    return moves

while tilt_platform() > 0: pass

[print(''.join(line)) for line in platform]

max, sum = len(platform), 0
for l, line in enumerate(platform):
    sum += line.count('O') * (max - l)
print('Task 1: %d' % sum) # 136 / 109638
