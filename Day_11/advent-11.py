
file_name, factor = "./Day_11/sample-11.1.txt", 99
file_name, factor = "./Day_11/input-advent-11.txt", 999999

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

# expand by storing added rows and columns
rows = [row_number for row_number,row in enumerate(universe) if sum(row) == 0]

cols = []
for x in reversed(range(len(universe[0]))):
    column = [universe[y][x] for y in range(len(universe)) ]
    if sum(column) == 0:
        cols.append(x)

rows.sort()
cols.sort()

# find galaxies
galaxies = []
for x in range(len(universe[0])):
    for y in range(len(universe)):
        if universe[y][x] != 0:
            galaxies.append((x, y))
      
distance = 0
distance2 = 0       
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        xs = [galaxies[i][0], galaxies[j][0]]
        ys = [galaxies[i][1], galaxies[j][1]]
        xs.sort()
        ys.sort()
        nx = len(list(filter(lambda r: r > xs[0] and r < xs[1], cols)))
        ny = len(list(filter(lambda c: c > ys[0] and c < ys[1], rows)))
        distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + nx + ny
        distance2 += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + nx * factor + ny * factor

print('Task 1: Sum of distances = %d' % distance) # 374 for sample, 9623138 for input
print('Task 2: Sum of distances = %d' % distance2) # 1030/8410 for sample, 726820169514 for input