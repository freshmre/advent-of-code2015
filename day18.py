def setcorners(grid):
    grid[0][0] = 1
    grid[0][-1] = 1
    grid[-1][0] = 1
    grid[-1][-1] = 1

def get_neighbors(row, col):
    n = 0
    for d_row in [-1, 0, 1]:
        for d_col in [-1, 0, 1]:
            nr, nc = row + d_row, col + d_col
            if within_bounds(nr, nc) and not (d_row == d_col == 0):
                n += inp[nr][nc]
    return n

def within_bounds(row, col):
    return row in range(len(inp)) and col in range(len(inp[0]))

def step():
    global inp

    newgrid = [inp[i].copy() for i in range(len(inp))]
    for row in range(len(inp)):
        for col in range(len(inp[0])):
            neighbors = get_neighbors(row, col)

            if (inp[row][col] == 1) and (neighbors not in (2, 3)):
                newgrid[row][col] = 0

            elif (inp[row][col] == 0) and (neighbors == 3):
                newgrid[row][col] = 1

    setcorners(newgrid)
    inp = newgrid

def geton(grid):
    return sum(sum(l) for l in grid)

inp = []

with open("inp.txt", "r") as f:
    while (l := f.readline().strip()):
        lights = [int(c == '#') for c in l]
        inp.append(lights)
    setcorners(inp)


for _ in range(100):
    step()

print(geton(inp))
