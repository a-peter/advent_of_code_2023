# source: https://topaz.github.io/paste/#XQAAAQBmAgAAAAAAAAA0m0pnuFI8c+qagMoNTEcTIfyUXGIEQsLiwfZiM5wZt1ZMMPcTKK2ft0d7lPLO5UIuq2zeAKsvhEDiXiexJAfl5J0KS2fWgRH6MCDPxL21uOltVidAmKlwyui3ec2wn9oG5cGiSPUIrWsNIJZxwHNq+hlFK07e6ez1Z8JELe5u/fSkJBLWMZ6Zh3LNVQo+rhPqUN8Q64ZerF1OxBKwM+fKlh59L7V3TXN1PxDYDh9DqnNPtfFrxo3QMALiw62NxgSRtQUhrCz49IAAqCrR4r484beFQXh7UEWodO8b8j06TV8o5buafcUC6niwgsXQnCLS6pWlAbEYjq2S532Zss7SYQdwb2ds/p3xawksAQpFV3ZfMPNubVFEPgmMG5ZjyAjJVb8Y+L1h3COoyWscXyeEHKpLhrU1flR3r2W54bG7CfpgcSfa4JZhYBYgufX2U5zHEM7HU3tU0eqd8/E8Tg6hR5ZeisTyyhyGjgdwsUw7BxyYHiiC4NME+2aaHs9wwvuZLKQ=

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