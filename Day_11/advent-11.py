

file_name = "./Day_11/sample-11.1.txt"
file_name = "./Day_11/input-advent-11.txt"

universe = [[x for x in line] for line in open(file_name).read().splitlines()]

# change to ints
universe_number = 1
for y,line in enumerate(universe):
    for x,col in enumerate(line):
        if col == '.':
            universe[y][x] = 0
        else:
            universe[y][x] = universe_number
            universe_number += 1

# expand
for y in reversed(range(len(universe))):
    if sum(universe[y]) == 0:
        universe.insert(y, [0] * len(universe[0]))

for x in reversed(range(len(universe[0]))):
    column = [universe[y][x] for y in range(len(universe)) ]
    if sum(column) == 0:
        for y in range(len(universe)):
            universe[y].insert(x, 0)

# find galaxies
galaxies = []
for x in range(len(universe[0])):
    for y in range(len(universe)):
        if universe[y][x] != 0:
            galaxies.append((x, y))
      
distance = 0          
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print('Task 1: Sum of distances = %d' % distance)
pass
