from functools import reduce
import math

input = []
input2 = []

for line in open('./Day_06/input-advent-06.1.txt'):
# for line in open('./Day_06/sample-06.1.txt'):
    input.append([int(i) for i in line[line.index(':') + 1:].split()])
    input2.append(int(line[line.index(':') + 1:-1].replace(' ', '')))

number_of_choices = []
for race in range(len(input[0])):
    choices_for_race = 0
    race_time = input[0][race]
    for down_time in range(race_time + 1):
        choices_for_race += int(down_time * (race_time - down_time) > input[1][race])
    number_of_choices.append(choices_for_race)

task_1 = reduce(lambda x,y: x * y, number_of_choices)
print('Task 1: %d' % task_1)
# should be 219849

#faster for task2:
time = input2[0]
distance = input2[1]

solution1 = (time/2) + math.sqrt((time * time)/4 - distance)
solution2 = (time/2) - math.sqrt((time * time)/4 - distance)

print(math.floor(solution1))
print(math.ceil(solution2))
print(math.floor(solution1) - math.ceil(solution2) + 1)
pass

race_time = input2[0]
choices_for_race = 0
for down_time in range(race_time + 1):
    # my_distance = down_time * (race_time - down_time)
    choices_for_race += int(down_time * (race_time - down_time) > input2[1])
print('Task 2: %d' % choices_for_race)
# should be 29432455
# time: 11 seconds