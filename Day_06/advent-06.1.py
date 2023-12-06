from functools import reduce
input = []

for line in open('./Day_06/input-advent-06.1.txt'):
# for line in open('./Day_06/sample-06.1.txt'):
    input.append([int(i) for i in line[line.index(':') + 1:].split()])

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