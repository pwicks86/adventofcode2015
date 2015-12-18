import copy
f = open("input.txt")
d = f.readlines()
rows = 100
cols = 100
grid = [[0 for x in range(cols+2)] for x in range(rows+2)]
next_grid = copy.deepcopy(grid)
row = 1
for l in d:
    col = 1
    for c in l:
        grid[row][col] = 1 if c == "#" else 0
        col += 1
    row += 1

for step in range(100):
    for row in range(1,101):
        for col in range(1,101):
            nsum = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    nsum += grid[row + i][col+j]
            on = grid[row][col]
            if on:
                next_grid[row][col] = 1 if nsum in [3,4] else 0
            else:
                next_grid[row][col] = 1 if nsum == 3 else 0
    grid, next_grid = next_grid, grid

gsum = 0
for g in grid:
    gsum += sum(g)

print(gsum)
