
cache = {}
cache_hit = 0
solve_count = 0
def solve_input(line: str, engines: list[int]) -> int:
    global cache_hit, solve_count
    solve_count += 1
    
    # exit if line too short for all engines.
    engines_size = sum(engines) + len(engines) - 1
    if (len(line) < engines_size): return 0
    
    # return result on cache hit
    if (line, tuple(engines)) in cache:
        cache_hit += 1
        return cache[(line, tuple(engines))]

    # if there are NO left-over '#' everything is consumed ->fit, else does not fit
    if len(engines) == 0:
        return 1 if "#" not in line else 0
    
    block_size = engines[0]
    total_positions = 0

    for i in range(len(line) - engines_size + 1):
        if (
            all(c != "." for c in line[i : i + block_size]) # may the next none-empty fields fit the lengt?
            # and (i == 0 or line[i - 1] != "#") # previous field is '?' (except of line-start) # REALLY NEEDED?
            and (
                i + block_size == len(line)     # fits end of line
                or line[i + block_size] != "#"  # or end sign is '?'
                )
        ):
            # block did fit. skip line for block length and next empty
            total_positions += solve_input(line[i + block_size + 1 :], engines[1:])

        if line[i] == '#': # if there is a '#', we're done
            break

    cache[(line, tuple(engines))] = total_positions

    return total_positions

file_name, s1, s2 = './Day_12/sample-12.1.txt', 21, 525152
file_name, s1, s2 = './Day_12/input-advent-12.txt', 7916, 37366887898686

# Read input
inputs = []
for line in open(file_name):
    engines, groups = line.split()
    inputs.append( (engines, [int(x) for x in groups.split(',')]) )

# [print(line) for line in inputs]

# print(max([solve_input(input) for input in inputs]))

total_1 = 0
total_2, times = 0, 5

for input in inputs:
    total_1 += solve_input(input[0], input[1])
    total_2 += solve_input('?'.join([input[0]] * times), input[1] * times)

print('Cache-hit: %d' % cache_hit)
print('recursions: %d' % solve_count)
print('Task 1: %d' % total_1) # 21     or 7916
print('Task 2: %d' % total_2) # 525152 or 37366887898686
if s1 != total_1 or s2 != total_2:
    print('FAIL!!! -----------------------------')