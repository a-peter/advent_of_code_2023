import re

sum = 0
for line in open('./Day_01/input-advent-01.1.txt'):
    all = re.findall('\d', line)
    combine = all[0] + all[-1]
    number = int(combine)
    sum += number

print('The sum is %d' % sum)

