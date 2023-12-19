import re

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