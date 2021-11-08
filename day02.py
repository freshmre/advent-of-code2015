with open("inp.txt", "r") as f:
    inp = f.read().splitlines()

# inp = ['2x3x4']
paper = ribbon = 0
for line in inp:
    x, y, z = list(map(int, line.split('x')))
    st = sorted([x, y, z])
    paper += 2 * (x*y + y*z + z*x) + st[0] * st[1]
    ribbon += x*y*z + (st[0] + st[1]) * 2

print(f"Needed (feet): paper {paper}, ribbon {ribbon}")