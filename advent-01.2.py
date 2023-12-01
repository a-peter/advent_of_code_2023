import re

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regex = re.compile('(?=(\d|' + '|'.join(numbers) + '))')

def string_to_num(str):
    if str in numbers:
        return numbers.index(str) + 1
    else:
        return int(str)

def match_to_sum(first, second):
    return string_to_num(first.group(1)) * 10 + string_to_num(second.group(1))

sum = 0
for line in open('input-advent-01.1.txt'):
    it = regex.finditer(line)
    first = next(it)
    last = first
    for m in it: last = m
    sum += match_to_sum(first, last)

print('The sum is %d' % sum)

