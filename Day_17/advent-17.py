import functools
import math

import numpy as np
from tqdm import trange
import heapq

# Annahme: Keine Kreuzung der Pfade!

file_name = './Day_17/sample-17.1.txt'
EAST,SOUTH,WEST,NORTH = range(4)
MAX_STEPS_FORWARD = 3

city = np.array([np.array([int(x) for x in line]) for line in open(file_name).read().splitlines()])
city_w = len(city[0]) # city.shape[1] = number of columns / x 
city_h = len(city) # city.shape[0] = number of rows / y
route = [(0,0)]
target = (city_w - 1, city_h - 1)
min_cost = 1_000_000_000


def step(location: tuple[int, int], direction: int) -> tuple[bool, tuple[int, int]]:
  if direction == EAST:
    new_x = location[0] + 1
    if not (new_x, location[1]) in route and new_x < city_w:
      return (True, (new_x, location[1]))
  elif direction == WEST:
    new_x = location[0] - 1
    if not (new_x, location[1]) in route and new_x > 0:
      return (True, (new_x, location[1]))
  elif direction == NORTH:
    new_y = location[1] - 1
    if not (location[0], new_y) in route and new_y > 0:
      return (True, (location[0], new_y))
  else:
    new_y = location[1] + 1
    if not (location[0], new_y) in route and new_y < city_h:
      return (True, (location[0], new_y))
  return (False, (-1, -1))

@functools.cache
def get_cost(location: tuple[int,int]) -> int:
  return city[location[1]][location[0]]

def print_route():
  grid = [['.' for x in range(city_w)] for y in range(city_h)]
  for r in route:
    grid[r[1]][r[0]] = '#'
  grid[city_h - 1][city_w - 1] = '*'
  [print(''.join(x)) for x in grid]
  print()

def move(direction: int, steps_forward: int, cost: int):
  global min_cost
  current_location = route[-1]

  if cost > min_cost:
    route.pop()
    return

  # step forward?
  if steps_forward < MAX_STEPS_FORWARD:
    possible, new_location = step(current_location, direction)
    if possible:
      if new_location == target:
        min_cost = min(min_cost, cost + get_cost(new_location))
        print_route()
        route.pop()
        return
      route.append(new_location)
      move(direction, steps_forward + 1, cost + city[new_location[1]][new_location[0]])

  # cw?
  new_direction = (direction + 1) % 4
  possible, new_location = step(current_location, new_direction)
  if possible:
    if new_location == target:
        min_cost = min(min_cost, cost + get_cost(new_location))
        print_route()
        route.pop()
        return
    route.append(new_location)
    move(new_direction, 1, cost + city[new_location[1]][new_location[0]])

  # ccw?
  new_direction = (direction - 1 + 4) % 4
  possible, new_location = step(current_location, new_direction)
  if possible:
    if new_location == target:
        min_cost = min(min_cost, cost + get_cost(new_location))
        print_route()
        route.pop()
        return
    route.append(new_location)
    move(new_direction, 1, cost + city[new_location[1]][new_location[0]])

  route.pop() # did not work :-(
  pass

# Directions:
Right, Down, Left, Up = (0, 1), (1, 0), (0, -1), (-1, 0)
Directions = [Right, Down, Left, Up]

def find_path(ciyt: list[list[int]], min_step: int, max_step: int) -> int:
  route = set()
  possible_steps = [(0, (0, 0), Right, 1), (0, (0, 0), Down, 1)]
  l_c = -1
  while len(possible_steps) > 0:
    cost, (x, y), direction, direction_count = heapq.heappop(possible_steps)

    if ((x,y), direction, direction_count) in route:
      continue
    else:
      route.add(((x,y), direction, direction_count))

    # test if in limits, maybe earlier?
    new_x, new_y = x + direction[1], y + direction[0]
    if new_x < 0 or new_x >= city_w or new_y < 0 or new_y >= city_h:
      continue # out of city, skip 

    new_cost = cost + get_cost((new_x, new_y))

    if min_step <= direction_count <= max_step:
      if new_x == city_w -1 and new_y == city_h - 1:
        return new_cost
      
    for d in Directions:
      # not reverse!
      if d[0] + direction[0] == 0 and d[1] + direction[1] == 0:
        continue
      new_d_count = direction_count + 1 if d == direction else 1
      if (d != direction and direction_count < min_step) or new_d_count > max_step:
        continue
      heapq.heappush(possible_steps, (new_cost, (new_x, new_y), d, new_d_count))


# while True:
# move(EAST, 0, city[0][0])

# [print(x, end='')) for line in city]

print('Cost 1:', find_path(city, 1, 3)) # ? / 970
# ? / 1149