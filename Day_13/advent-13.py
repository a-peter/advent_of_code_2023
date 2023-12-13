import functools
import math

@functools.cache
def compare_lines(line1: str, line2: str) -> bool:
    return line1 == line2

def is_symmetric(lines: list[str]) -> bool:
    # Test, if all inner lines are pair-wise symmetric, no uneven number of lines allowed.
    if len(lines) % 2 == 1:
        return False
    if len(lines) == 2:
        return compare_lines(lines[0], lines[1])
    else:
        return is_symmetric(lines[1:-1])

def find_symmetry(pattern: list[list[str]], factor: int) -> list[tuple[int, int]]:
    lines = [''.join(line) for line in pattern]

    solutions = []
    i = 0
    found = False
    while i < len(lines) - 1:
    # for i in range(len(lines) - 1):
        for j in range(len(lines) - 1, i, -1):
            if compare_lines(lines[i], lines[j]):
                if is_symmetric(lines[i:j+1]):
                    width = j - i + 1
                    x1 = int(i + width / 2)
                    x2 = x1 + 1
                    # solutions.append(((i, j), (x1, x2), width))
                    solutions.append(((x1, x2), width, x1 * factor))
                    found = True
                    break
        if found:
            i = j+1
        else:
            i += 1
        found = False
    return solutions
                
def solve_puzzle(pattern: list[list[str]], factor: int) -> list[tuple[int, int]]:
    return find_symmetry(pattern, factor)

file_name = './Day_13/sample-13.1.txt'
file_name = './Day_13/input-advent-13.txt'

input = [line for line in open(file_name).read().splitlines()]
empty = [-1] + [i for i, line in enumerate(input) if len(line) == 0] + [len(input)]

result = 0
for index in range(len(empty) - 1):
    pattern = input[empty[index] + 1:empty[index + 1]]
    solutions_1 = solve_puzzle(pattern, 100) # add 
    solutions_1 += solve_puzzle([list(x) for x in zip(*pattern)], 1)
    print(solutions_1)
    m = max(solutions_1, key = lambda x: x[1])
    print(m)
    result += m[2]

print('Task 1: %d' % result)
