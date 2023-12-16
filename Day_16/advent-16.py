
UP, RIGHT, DOWN, LEFT = range(4)
LOCATION, DIRECTION = range(2)
COLUMN, ROW = range(2)
map_direction = {'/': [RIGHT, UP, LEFT, DOWN], '\\': [LEFT, DOWN, RIGHT, UP]}


def pass_field(beam: list[list[int], int]):
  match beam[DIRECTION]:
    case 0: beam[LOCATION][ROW] -= 1
    case 1: beam[LOCATION][COLUMN] += 1
    case 2: beam[LOCATION][ROW] += 1
    case 3: beam[LOCATION][COLUMN] -= 1

def location_inside(position: list[int], width: int, height: int) -> bool:
  return position[ROW] >= 0 and position[ROW] < height and position[COLUMN] >= 0 and position[COLUMN] < width

# def move(beam: list[list[int], int]):
#   match beam[DIRECTION]
#     case 0: beam[LOC]

file_name = './Day_16/sample-16.1.txt'
file_name = './Day_16/input-advent-16.txt'

contraption = [line for line in open(file_name).read().splitlines()]
width = len(contraption[0])
height = len(contraption)
energized = [[0 for col in range(width)] for line in range(height)]

def turn_beam(beam: list[list[int], int], current_field: int, split_beam: bool) -> list[list[int], int]:
  new_beam = None
  _, direction = beam[LOCATION], beam[DIRECTION]
  if current_field == '.' or (current_field == '|' and direction in [UP, DOWN]) or (current_field == '-' and direction in [LEFT, RIGHT]):
    pass_field(beam)
  elif current_field == '|' and (direction == RIGHT or direction == LEFT):
    beam[DIRECTION] = UP
    if split_beam:
      new_beam = [[i for i in beam[LOCATION]], DOWN]
      pass_field(new_beam)
    pass_field(beam)
    # beams.append(new_beam)
  elif current_field == '-' and (direction == UP or direction == DOWN):
    beam[DIRECTION] = LEFT
    if split_beam:
      new_beam = [[i for i in beam[LOCATION]], RIGHT]
      pass_field(new_beam)
    pass_field(beam)
    # beams.append(new_beam)
  elif current_field == '/' or current_field == '\\':
    beam[DIRECTION] = map_direction[current_field][beam[DIRECTION]]
    pass_field(beam)
  else:
    pass # Why are we here???
  return new_beam

start_beam = [[0,0], RIGHT] # [[x,y], direction]

beams = [start_beam]
moved_beams = 1
loop_counter = 0
loop_index = 0
while moved_beams > 0 and loop_counter < 40:
  loop_index += 1
  if loop_index % 10 == 0:
    print('loop %d, %d beams, %d energized' % (loop_index, len(beams), energizer_counter))
  energizer_counter = 0
  moved_beams = 0
  for beam in beams:
    location, direction = beam[LOCATION], beam[DIRECTION]

    # remove beams out of field
    if not location_inside(location, width, height):
      beams.remove(beam)
      continue

    # energize cell
    if not energized[location[ROW]][location[COLUMN]]:
      energized[location[ROW]][location[COLUMN]] = 1
      energizer_counter += 1
      loop_counter = 0
      split_beam = True
    else:
      split_beam = False

    moved_beams += 1

    # turn if necessary, create new beam, IF!!! no beam was created here
    current_field = contraption[location[ROW]][location[COLUMN]]
    # new_beam = turn_beam(beam, current_field, split_beam)

    if current_field == '.' or (current_field == '|' and direction in [UP, DOWN]) or (current_field == '-' and direction in [LEFT, RIGHT]):
      pass_field(beam)
    elif current_field == '|' and (direction == RIGHT or direction == LEFT):
      beam[DIRECTION] = UP
      if split_beam:
        new_beam = [[i for i in beam[LOCATION]], DOWN]
        pass_field(new_beam)
        beams.append(new_beam)
      pass_field(beam)
    elif current_field == '-' and (direction == UP or direction == DOWN):
      beam[DIRECTION] = LEFT
      if split_beam:
        new_beam = [[i for i in beam[LOCATION]], RIGHT]
        pass_field(new_beam)
        beams.append(new_beam)
      pass_field(beam)
    elif current_field == '/' or current_field == '\\':
      beam[DIRECTION] = map_direction[current_field][beam[DIRECTION]]
      pass_field(beam)
    else:
      pass # Why are we here???
  # Remove beams out of field
  if energizer_counter == 0:
    loop_counter += 1
  for beam in beams:
    if not location_inside(beam[LOCATION], width, height):
      beams.remove(beam)

energized_fields = sum([sum(x) for x in energized])
print('Task 1: %d energized' % energized_fields) # 46 / 7496
# [print(line) for line in contraption]