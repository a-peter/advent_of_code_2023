import numpy as np

file_name = './Day_22/sample-22.1.txt'
file_name = './Day_22/input-22.txt'

bricks = np.fromregex(file_name, r'(\d+)', [('',int)]).reshape(-1, 6).astype(int)
max_x, max_y = np.amax(bricks, axis=0)[3:5]

# The blocks are all straight. No Tetris like blocks.
def drop(bricks, desintegrate:int = None) -> tuple[int,int]:
    tops = np.zeros((max_x + 1, max_y + 1), dtype=int)
    falls = 0

    for i, (x1,y1,z1, x2,y2,z2) in enumerate(bricks):
        if i == desintegrate: continue
        height = z2 - z1 + 1 # height of the brick

        max_height = tops[x1:x2+1, y1:y2+1].max() # maximum height in area of brick
        tops[x1:x2+1, y1:y2+1] = max_height + height

        bricks[i] = x1,y1,max_height+1, x2,y2,max_height+height # move brick to new position
        falls += max_height+1 < z1

    return bricks if desintegrate==None else (int(not falls),falls)

bricks = drop(bricks[bricks[:, 2].argsort()])
result = [drop(bricks.copy(), i) for i in range(len(bricks))]

# axis = 0 -> sum first axis, here: sum all first of tuples and all second of tuples. Result is an array.
print(*np.sum(result, axis=0)) # [5, 7] / [488, 79465]