
def compare_lines(line1: str, line2: str) -> int:
    return sum([int(not i==j) for i,j in zip(line1, line2)])
               
def solve(pattern: list[str], smudge: int) -> int:
    pattern_h = len(pattern)
    # tests if pattern is symmetric and returns the row for the symmetry
    for i in range(len(pattern) - 1):
        symm_h = min( (i+1)*2 , (pattern_h - i - 1) * 2)
        start = i - symm_h//2 + 1
        end = start + symm_h - 1

        if sum([compare_lines(pattern[start+j], pattern[end-j]) for j in range(symm_h//2)]) == smudge:
            return i+1
    return 0

file_name = './Day_13/sample-13.1.txt'
file_name = './Day_13/input-advent-13.txt'

data = [ [x for x in s.split('\n') if x] for s in open(file_name).read().split('\n\n')]
data_t = [list("".join(x) for x in zip(*grid)) for grid in data]

total1 = 0
total2 = 0
for index in range(len(data)):
    total1 += solve(data[index], 0) * 100 + solve(data_t[index], 0)
    total2 += solve(data[index], 1) * 100 + solve(data_t[index], 1)
    

print('Task 1: %d' % total1) # 405 / 34918
print('Task 2: %d' % total2) # 400 / 33054
