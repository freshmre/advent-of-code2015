import sys

with open("day06.txt", "r") as f:
    rinp = f.readlines()
    # rinp = ['turn on 0,0 through 0,0']

def run(ins):
    op = ins[0]
    if op == 'on':
        f = lambda l: l + 1
    elif op == 'off':
        f = lambda l: l - 1 if l > 1 else 0
    elif op == 'toggle':
        f = lambda l: l + 2
    else:
        print("something went wrong")
        sys.exit(1)

    for row in range(ins[1][0], ins[1][1] + 1):
        for col in range(ins[2][0], ins[2][1] + 1):
            grid[row][col] = f(grid[row][col])

inp = []
for ins in rinp:
    ins = ins.split()
    # print(ins)
    tgl = len(ins) == 4
    state = ins[1-tgl]
    start = ins[2-tgl].split(',')
    end = ins[4-tgl].split(',')
    xrange = (int(start[0]), int(end[0]))
    yrange = (int(start[1]), int(end[1]))
    inp.append([state, xrange, yrange])

def on():
    s = 0
    for row in range(1000):
        for col in range(1000):
            s += grid[row][col]
    return s


grid = [[0] * 1000 for _ in range(1000)]
print(on())

for ins in inp:
    run(ins)

print(on())

# print(inp)