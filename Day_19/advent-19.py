
file_name = './Day_19/sample-19.1.txt'

workflow, parts_text = open(file_name).read().split('\n\n')

parts = []
for line in parts_text.splitlines():
    parts.append({c:int(d) for (c,d) in [[cat for cat in part.split('=')] for part in line[1:-1].split(',')]})

print(workflow)
print(parts)