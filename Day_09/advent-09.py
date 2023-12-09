
# file_name = './Day_09/sample-09.1.txt'
file_name = './Day_09/input-advent-09.txt'

inputs = []
for line in open(file_name):
  inputs.append([int(i) for i in line.split()])

sum = 0
for measure in inputs:
  calculus = [measure]
  # print(calculus)
  while True:
    all_zero = True
    line = calculus[-1]
    new_line = []
    for i in range(len(line) - 1):
      diff = line[i+1] - line[i]
      new_line.append(diff)
      all_zero = all_zero and diff == 0
    calculus.append(new_line)
    if all_zero:
      break
  new_value = 0
  for i in range(len(calculus)):
    new_value += calculus[-(i+1)][-1]
  sum += new_value

# 18 28 68
print('Task 1: %d' % sum)