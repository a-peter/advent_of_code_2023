import functools
import math

@functools.cache
def compare_lines(line1: str, line2: str) -> bool:
    return line1 == line2
               
def solve(pattern: list[str]) -> int:
    pattern_h = len(pattern)
    # tests if pattern is symmetric and returns the row for the symmetry
    for i in range(len(pattern) - 1):
        symm_h = min( (i+1)*2 , (pattern_h - i - 1) * 2)
        start = i - symm_h//2 + 1
        end = start + symm_h - 1
        # print(start, end)
        symm = True
        for j in range(symm_h//2):
            symm &= compare_lines(pattern[start + j], pattern[end - j])
        if symm:
            return i+1
    return 0

file_name = './Day_13/sample-13.1.txt'
file_name = './Day_13/input-advent-13.txt'

data = [ [x for x in s.split('\n') if x] for s in open(file_name).read().split('\n\n')]
data_t = [list("".join(x) for x in zip(*grid)) for grid in data]

total = 0
for index in range(len(data)):
    s1 = solve(data[index])
    s2 = solve(data_t[index])
    # print(s1, s2)
    total += s1 * 100 + s2

print('Task 1: %d' % total)
exit(0)
