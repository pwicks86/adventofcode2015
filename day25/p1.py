#To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075.
frow = 2981
fcol = 3075
mat_size = fcol*2
matrix = [[0 for x in range(mat_size)] for x in range(mat_size)]
matrix[0][0] = 20151125
prev_row = 0
prev_col = 0
for start_row in range(1, mat_size):
    fill_num = start_row + 1
    start_col = 0
    for f in range(fill_num):
        col = start_col + f
        row = start_row - f
        prev_val = matrix[prev_row][prev_col]
        matrix[row][col] = (prev_val * 252533) % 33554393
        prev_row = row
        prev_col = col

print(matrix[frow-1][fcol-1])

