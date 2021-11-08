import re

with open("inp.txt", "r") as f:
    pattern = r'row (\d+).*column (\d+)'
    inp = f.read()
    row, col = re.search(pattern, inp).groups()
    row, col = int(row), int(col)

def find_order(col, row):
    """Find the order of a cell in diagonally filled grid"""
    return arithmetic_sum(0, col + row - 2) + col

def arithmetic_sum(start, end, r=1):
    mid = (start + end) / 2
    n = 1 + (end - start) // r
    return round(n * mid)

def find_cell_val(n):
    cell_val = 20151125
    for _ in range(n - 1):
        cell_val = (cell_val * 252533) % 33554393
    return cell_val

assert find_order(6, 1) == 21
assert find_order(4, 1) == 10
assert find_order(1, 1) == 1
assert find_order(1, 6) == 16

cell_n = find_order(col, row)
print(find_cell_val(cell_n))
