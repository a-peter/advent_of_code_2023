# source: https://github.com/AshGriffiths/advent_of_code/blob/main/2023/day_thirteen/day13.py

file_name = './Day_13/sample-13.1.txt'
file_name = './Day_13/input-advent-13.txt'

r = []
def check_symmetry(grid: list[str], allowed_smudges: int = 0) -> int:
    global r
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    for col in range(no_of_cols - 1):
        error_count = 0
        for split_col in range(no_of_cols):
            left = col - split_col
            right = col + 1 + split_col
            if 0 <= left < right < no_of_cols:
                r.append((left, right))
                for row in range(no_of_rows):
                    if grid[row][left] != grid[row][right]:
                        error_count += 1
        if error_count == allowed_smudges:
            print(r)
            return col + 1
        r = []
    return 0


with open(file_name, "r") as input:
    grids = [row for row in [s.splitlines() for s in input.read().split("\n\n")]]
    transposed_grids = [list("".join(x) for x in zip(*grid)) for grid in grids]
    p1_total = 0
    p2_total = 0

    # APE42
    for i in range(len(grids)):
        x1 = check_symmetry(grids[i])
        x2 = check_symmetry(transposed_grids[i])
        p1_total += x1
        p1_total += 100 * x2
        print(i, x1, x2)

    # for grid in grids:
    #     p1_total += check_symmetry(grid)
    #     # p2_total += check_symmetry(grid, 1)
    # for t_grid in transposed_grids:
    #     p1_total += 100 * check_symmetry(t_grid)
    #     # p2_total += 100 * check_symmetry(t_grid, 1)

    
    print(f"Part One : {p1_total}")
    print(f"Part Two : {p2_total}")

# 34918
# 33054