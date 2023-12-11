
file_name, factor = "./Day_11/sample-11.1.txt", 99
# file_name, factor = "./Day_11/input-advent-11.txt", 999999

# read input data
universe = [[0 if x == '.' else 1 for x in line] for line in open(file_name).read().splitlines()]

# expand by storing added rows and columns
added_rows = [row_number for row_number,row in enumerate(universe) if sum(row) == 0]
added_cols = [col_number for col_number,col in enumerate(zip(*universe)) if sum(col) == 0]

# find galaxies
galaxies = [(x,y) for y in range(len(universe)) for x in range(len(universe[0])) if universe[y][x] != 0]

# calculate distances. Because the shortest path is a sequence of left/right/down/up instructions
# it is the same to calculate the distance for x and for y.
distance1 = 0
distance2 = 0       
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        xs = sorted([galaxies[i][0], galaxies[j][0]])
        ys = sorted([galaxies[i][1], galaxies[j][1]])
        nx = len(list(filter(lambda r: r > xs[0] and r < xs[1], added_cols))) # number of expanded columns
        ny = len(list(filter(lambda c: c > ys[0] and c < ys[1], added_rows))) # number of expanded rows
        distance1 += xs[1] - xs[0] + ys[1] - ys[0] + nx + ny
        distance2 += xs[1] - xs[0] + ys[1] - ys[0] + (nx + ny) * factor

print('Task 1: Sum of distances = %d' % distance1) # 374 for sample, 9623138 for input
print('Task 2: Sum of distances = %d' % distance2) # 1030/8410 for sample, 726820169514 for input