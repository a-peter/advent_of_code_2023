import re

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regex = re.compile('(\d|' + '|'.join(numbers) + ')')

def string_to_num(str):
    if str in numbers:
        return numbers.index(str) + 1
    else:
        return int(str)

def match_to_sum(first, second):
    return string_to_num(first) * 10 + string_to_num(second)


sum = 0
for line in open('input-advent-01.1.txt'):
    first = regex.search(line)
    f = first
    # The strings might overlap like: eightwo. This has to evaluated
    # as 'eight' *and* 'two'
    while f:
        last = f
        line = line[last.start()+1:]
        f = regex.search(line)
        
    sum += match_to_sum(first.group(), last.group())

print('The sum is %d' % sum)

