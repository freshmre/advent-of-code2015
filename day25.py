r, c = 3010, 3019
cell_n = (r + c - 2) * (r + c - 1) // 2 + c

cell_val = 20151125
for _ in range(cell_n - 1):
    cell_val = (cell_val * 252533) % 33554393

print(cell_val)
