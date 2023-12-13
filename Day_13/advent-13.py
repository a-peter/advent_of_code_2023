import functools
import math

@functools.cache
def compare_lines(line1: str, line2: str) -> bool:
    return line1 == line2

def is_symmetric(pattern: list[str]) -> bool:
    for i in range(int(len(pattern)/2)):
        if not compare_lines(pattern[i], pattern[len(pattern) - i - 1]):
            return False
    return True
                
def solve_puzzle(pattern: list[str], factor: int) -> int:
    for i in range(2):
        if is_symmetric(pattern[i:len(pattern) - (1 - i)]):
            return int(len(pattern) / 2) + i
    return 0

file_name = './Day_13/sample-13.1.txt'
file_name = './Day_13/input-advent-13.txt'

data = [ [x for x in s.split('\n') if x] for s in open(file_name).read().split('\n\n')]
data_t = [list("".join(x) for x in zip(*grid)) for grid in data]

result = 0
for p in range(len(data)):
    result += solve_puzzle(data[p], 1)
    result += solve_puzzle(data_t[p], 1) * 100

print('Task 1: %d' % result) # 405 / 34918
