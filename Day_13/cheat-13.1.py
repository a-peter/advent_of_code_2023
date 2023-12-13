# source: https://github.com/sayan01/advent-of-code-2023/blob/master/13/p.py

from Levenshtein import distance as D
input = [[x for x in s.split('\n')if x]for s in open('./Day_13/input-advent-13.txt').read().split('\n\n')]
# print(len(S))
# print(S)
def c(pattern: list[tuple[str]],d=0):
  r = range(1, len(pattern[0]))
  return next((i for i in r if sum(D(*zip(*zip(row[:i][::-1],row[i:]))) for row in pattern)==d),0)

[print( sum(c(list(zip(*s)),p) for s in input) * 100 + sum(c(pattern,p) for pattern in input)) for p in [0,1]]
# 34918
# 33054