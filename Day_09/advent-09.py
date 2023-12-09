
file_name = './Day_09/sample-09.1.txt'
# file_name = './Day_09/input-advent-09.txt'

inputs = [[int(i) for i in line.split()] for line in open(file_name).read().splitlines()]

sum1, sum2 = 0, 0
for measure in inputs:
  history = [measure]
  while True:
    history.append([j - i for i,j in zip(history[-1], history[-1][1:])])
    if all(e == 0 for e in history[-1]):
      break

  sum1 += sum([row[-1] for row in history]) # new_value

  new_value_front = 0
  for i in range(len(history)):
    new_value_front = history[-(i+1)][0] - new_value_front
  sum2 += new_value_front

# sample data: 114 and 2
# real data. 1842168671 and 903

print('Task 1: %d' % sum1)  
print('Task 2: %d' % sum2)