
# file_name = "./Day_10a/sample-10.1.txt"
# file_name = "./Day_10a/sample-10.2.txt"
# file_name = "./Day_10a/sample-10.3.txt"
# file_name = "./Day_10a/sample-10.4.txt"
file_name = "./Day_10a/input-10.txt"
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
possible_movements = {
    '|': ['|7FS', '',     '|LJS', ''    ],
    '-': ['',     '-J7S', '',     '-LFS'],
    'L': ['|7FS', '-J7S', '',     ''    ],
    'J': ['|7FS', '',     '',     '-LFS'],
    '7': ['',     '',     '|LJS', '-LFS'],
    'F': ['',     '-J7S', '|LJS', ''    ],
    'S': ['|7FS', '-J7S', '|LJS', '-LFS']
}
replace_s = {1: 'L', 2: '|', 3: 'J', 12: 'F', 13: '-', 23: '7'}

# Find the start point of the pipe
def find_start(maze: list[str]) -> tuple[int, int]:
    for y,line in enumerate(maze):
        i = line.find('S')
        if i != -1:
            return (i,y)

# create a list of possible neighbours, taking into account the last movement.
# don't go back!
def possible_neighbours(location: tuple[int, int], movement: int) -> list[tuple[int, int, int]]:
    neighbours = [(location[0], location[1]-1, NORTH), (location[0]+1, location[1], EAST), (location[0], location[1]+1, SOUTH), (location[0]-1, location[1], WEST)]
    if movement != -1:
        index = (movement + 2) % 4
        del neighbours[index]
    return neighbours

# Test if a move is possible
def move_is_possible(maze: list[str], curr: str, x: int, y: int, movement: int):
    return maze[y][x] in possible_movements[curr][movement]

# Go to the next field from the current one
def next_field(maze: list[str], location: tuple[int, int], neighbours: list[tuple[int, int]]):
    x,y = location
    for nx,ny,movement in neighbours:
        if move_is_possible(maze, maze[y][x], nx, ny, movement):
            return ((nx, ny), movement) 

# Read maze and enhace by empty frame
maze = ['.' + line.strip() + '.' for line in open(file_name).readlines()]
maze.insert(0, '.' * len(maze[0]))
maze.append('.' * len(maze[0]))

#######################
# Task 

# Find the start point
start = find_start(maze)

movement = -1
location = start
path = [start]
while True:
    location, movement = next_field(maze, location, possible_neighbours(location, movement))
    path.append(location)
    if location == start:
        break

print('Task 1: Length = %d' % (len(path) / 2)) # 4 / 8 / 6956

#######################
# Task 2

def replace_start(maze: list[str], start: tuple[int,int]):
    neighbours = possible_neighbours(start, -1)
    all_neighbours = [d for x,y,d in neighbours if maze[y][x] != '.' and move_is_possible(maze, 'S', x,y,d)]
    x,y = start
    maze[y] = maze[y][:x] + replace_s[all_neighbours[0] * 10 + all_neighbours[1]] + maze[y][x+1:]

# Clean maze: All non-path elements to '.'
for x in range(len(maze[0])):
    for y in range(len(maze)):
        if (x,y) not in path:
            maze[y] = maze[y][:x] + '.' + maze[y][x+1:]
replace_start(maze, start)
# [print(line) for line in maze]


number_of_inside = 0
max_x = len(maze[0])
for y in range(len(maze)):
    inside = False
    x = 0
    while x < max_x:
        if maze[y][x] == '|':
            inside = not inside
        elif maze[y][x] == 'F':
            inside = not inside
            while maze[y][x+1] == '-':
                x += 1
            if maze[y][x+1] in '7':
                inside = not inside
            x += 1
        elif maze[y][x] == 'L':
            inside = not inside
            while maze[y][x+1] == '-':
                x += 1
            if maze[y][x+1] in 'J':
                inside = not inside
            x += 1
        else:
            if inside:
                number_of_inside += 1
                maze[y] = maze[y][:x] + 'I' + maze[y][x+1:]
        x += 1

# print()
# [print(line) for line in maze]
# print()
print('Task 2: Number of I = %d' % number_of_inside) 
# sample-10.3: 4
# sample-10.4: 8
# input      : 6956

