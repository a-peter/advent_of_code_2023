
file_name = './Day_10/sample-10.txt'
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

# Tiles that may connect when NORT/EAST/SOUTH/WEST of current tile
connects = [
  ['|', '7', 'F'],
  ['-', 'J', '7'],
  ['|', 'L', 'J'],
  ['-', 'L', 'F']
]
neighbours = {
  '|': [['|','7','F','S'], [],                ['|','L','J','S'], []               ],
  '-': [[],                ['-','J','7','S'], [],                ['-','F','L','S']],
  'L': [['|','7','F','S'], ['-','J','7','S'], [],                []               ],
  'J': [['|','7','F','S'], [],                [],                ['-','L','F','S']],
  '7': [[],                [],                ['|','L','J','S'], ['-','L','F','S']],
  'F': [[],                ['-','J','7','S'], ['|','L','J','S'], []               ],
  'S': [['|','7','F'],     ['-','J','7'],     ['|','L','J'],     ['-','L','F']    ]
}

array2D = [['.'] + list(line) + ['.'] for line in open(file_name).read().splitlines()]
array2D.insert(0, ['.'] * len(array2D[0]))
array2D.append(['.'] * len(array2D[0]))

width, height = len(array2D[0]), len(array2D)

def find_start():
  for y, line in enumerate(array2D):
    for x, c in enumerate(line):
      if line[x] == 'S':
        return x,y

def check(x, y):
  # if array2D[y][x] in ['.', 'S']:
  #   return
  if y > 0: # North
    if array2D[y-1][x] not in neighbours[array2D[y][x]][NORTH]:
      array2D[y-1][x] = '.'
  if x < width - 1: # East
    if array2D[y][x+1] not in neighbours[array2D[y][x]][EAST]:
      array2D[y][x+1] = '.'
  if y < height - 1: # South
    if array2D[y+1][x] not in neighbours[array2D[y][x]][SOUTH]:
      array2D[y+1][x] = '.'
  if x > 0: # West
    if array2D[y][x-1] not in neighbours[array2D[y][x]][WEST]:
      array2D[y][x-1] = '.'

(x,y) = find_start()
print('Start at %d, %d' % (x, y))

path = []
posX, posY = x, y 
while True:
   check(x,y,NORTH)


# Find the loop
for x in range(len(array2D[0])):
  for y in range(len(array2D)):
    check(x,y)
    pass

pass
