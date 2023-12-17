import numpy as np
from tqdm import trange
import heapq

file_name = './Day_17/sample-17.1.txt'
file_name = './Day_17/sample-17.2.txt'
file_name = './Day_17/input-advent-17.txt'

city = np.array([np.array([int(x) for x in line]) for line in open(file_name).read().splitlines()])
city_w = city.shape[1] # number of columns / x 
city_h = city.shape[0] # number of rows / y

# Directions:
Right, Down, Left, Up = (1, 0), (0, 1), (-1, 0), (0, -1)
Directions = [Right, Down, Left, Up]

def find_path(ciyt: list[list[int]], min_step: int, max_step: int) -> int:
  route = set()
  possible_steps = [(0, (0, 0), Right, 1), (0, (0, 0), Down, 1)]
  while len(possible_steps) > 0:
    cost, (x, y), direction, direction_count = heapq.heappop(possible_steps)

    # test if in limits, maybe earlier?
    new_x, new_y = x + direction[0], y + direction[1]
    if new_x < 0 or new_x >= city_w or new_y < 0 or new_y >= city_h:
      continue # out of city, skip 

    # Already visited? Skip
    if ((x,y), direction, direction_count) in route:
      continue
    else:
      route.add(((x,y), direction, direction_count))

    new_cost = cost + city[new_y, new_x]

    if min_step <= direction_count <= max_step:
      if new_x == city_w -1 and new_y == city_h - 1:
        return new_cost
      
    for d in Directions:
      # not reverse!
      if d[0] + direction[0] == 0 and d[1] + direction[1] == 0:
        continue
      new_d_count = direction_count + 1 if d == direction else 1
      # Go at least min steps in one direction, not more than max_steps
      if (d != direction and direction_count < min_step) or new_d_count > max_step:
        continue
      heapq.heappush(possible_steps, (new_cost, (new_x, new_y), d, new_d_count))


print('Cost 1:', find_path(city, 1, 3)) # 102 / 970
print('Cost 2:', find_path(city, 4, 10)) # 94 / 1149