import re
import functools

file_name = './Day_19/sample-19.1.txt'
file_name = './Day_19/input-advent-19.txt'
workflow_text, parts_text = open(file_name).read().split('\n\n')

# extract parts from input
parts = []
for line in parts_text.splitlines():
    parts.append({c:int(d) for (c,d) in [[cat for cat in part.split('=')] for part in line[1:-1].split(',')]})

# extract workflows from input
reg1 = r'(\w+){(.*),(\w+)}'
reg2 = r'(\w)(<|>)(\d+):(\w+)'
workflow = dict()
for line in workflow_text.splitlines():
    name, _, end = re.findall(reg1, line)[0]
    rules =[(cat,op,int(val),dest) for cat,op,val,dest in re.findall(reg2, line)]
    workflow[name] = (rules, end)

##############################
# Task 1

operators = {'<': lambda x,y: x < y, '>': lambda x,y: x > y}

# execute a workflow rule for a part
def process(part: dict[str: int], wf: tuple[list[tuple[str,str,int,str]], str]) -> bool:
    for cat,op,val,target in wf[0]:
        if operators[op](part[cat], val):
            if target == 'A': return True
            elif target == 'R': return False
            else: return process(part, workflow[target])
    if wf[1] == 'A': return True
    elif wf[1] == 'R': return False
    else: return process(part, workflow[wf[1]])

ratings = sum([sum(part.values()) for part in parts if process(part, workflow['in'])])
print('Task 1: %d' % ratings) # 19114 / 323625

##############################
# Task 2

sum_of_pathes = 0
def check_ranges(ranges: dict[str, list[int]], wf):
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
        if target == 'A':
            product = functools.reduce(lambda x,y: x*y, [x[1]-x[0]+1 for x in ranges_copy.values()], 1)
            sum_of_pathes += product
        elif target == 'R':
            pass
        else:
            check_ranges(ranges_copy, workflow[target])
    if wf[1] == 'A':
        product = functools.reduce(lambda x,y: x*y, [x[1]-x[0]+1 for x in leftover.values()], 1)
        sum_of_pathes += product
    elif wf[1] == 'R':
        pass
    else:
        check_ranges(leftover, workflow[wf[1]])

start_ranges = {cat:range for cat,range in zip(list('xmas'),[[1,4000]]*4)}

check_ranges(start_ranges, workflow['in'])
print('Task 2: %d' % sum_of_pathes) # 167409079868000 / 127447746739409