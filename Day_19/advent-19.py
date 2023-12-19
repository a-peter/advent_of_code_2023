import re
import functools

file_name = './Day_19/sample-19.1.txt'
file_name = './Day_19/input-advent-19.txt'

workflow_text, parts_text = open(file_name).read().split('\n\n')

parts = []
for line in parts_text.splitlines():
    parts.append({c:int(d) for (c,d) in [[cat for cat in part.split('=')] for part in line[1:-1].split(',')]})

wf_reg = re.compile('(\w+)\{(.*)\}')
rule_reg = re.compile('(\w+)(<|>)(\d+):(\w+)')
workflow = {}
for line in workflow_text.splitlines():
    match = wf_reg.match(line)
    # print(match.group(0), match.group(1), match.group(2).split(','))
    rules = [(cat,op,int(val),dest) for cat,op,val,dest  in [rule_reg.match(rule).groups() for rule in match.group(2).split(',') if ':' in rule]]
    workflow[match.group(1)] = (rules, match.group(2).split(',')[-1])

# print(workflow)
# print(parts)

lt = lambda x,y: x < y
gt = lambda x,y: x > y
ops = {'<': lt, '>': gt}

def process(part: dict[str: tuple[list[tuple[str,str,int,str]], str]], wf) -> bool:
    for cat,op,val,target in wf[0]:
        # print(cat,op,val,target)
        if ops[op](part[cat], val):
            if target == 'A': return True
            elif target == 'R': return False
            else: return process(part, workflow[target])
    if wf[1] == 'A': return True
    elif wf[1] == 'R': return False
    else: return process(part, workflow[wf[1]])

ratings = 0
for part in parts:
    if process(part, workflow['in']):
        ratings += sum(part.values())
        pass

print('Task 1: %d' % ratings) # 19114 / 323625

##############################
# Task 2

sum_of_pathes = 0
def check_ranges(ranges: dict[str, list[int]], wf, path: str):
    global sum_of_pathes
    leftover = {k:[x for x in v] for (k,v) in ranges.items()}
    for cat,op,val,target in wf[0]:
        ranges_copy = {k:[x for x in v] for (k,v) in leftover.items()}
        if op == '<':
            ranges_copy[cat][1] = val - 1
            leftover[cat][0] = val
        else:
            ranges_copy[cat][0] = val + 1
            leftover[cat][1] = val
        if ranges_copy[cat][0] > ranges_copy[cat][1]:
            continue
        if target == 'A':
            product = functools.reduce(lambda x,y: x*y, [x[1]-x[0]+1 for x in ranges_copy.values()], 1)
            sum_of_pathes += product
            print(path, product, ranges_copy)
        elif target == 'R':
            pass
        else:
            check_ranges(ranges_copy, workflow[target], path + ' -> ' + target)
    if wf[1] == 'A':
        product = functools.reduce(lambda x,y: x*y, [x[1]-x[0]+1 for x in leftover.values()], 1)
        sum_of_pathes += product
        print(path, product, leftover)
    elif wf[1] == 'R':
        pass
    else:
        check_ranges(leftover, workflow[wf[1]], path + '* ->' + wf[1])

    pass

ranges = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

wf = workflow['in']
check_ranges(ranges, wf, 'in')
print('Task 2: %d' % sum_of_pathes)