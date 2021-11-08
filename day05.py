from string import ascii_lowercase as al

with open("day05.txt", "r") as f:
    inp = f.read().strip()

def isvalid(pw):
    return r1(pw) and r2(pw) and r3(pw)

def r1(pw):
    forb = ['i', 'o', 'l']
    for l in forb:
        if l in pw:
            return False
    return True


def r2(pw):
    for i in range(len(pw) - 3):
        x, y, z = toint(pw[i]), toint(pw[i + 1]), toint(pw[i + 2])
        if x == (y - 1) and y == (z - 1):
            return True
    return False

def r3(pw):
    p = c = 0
    while p < (len(pw) - 1):
        if pw[p] == pw[p+1]:
            c += 1
            p += 2
        else:
            p += 1
    return c >= 2

def toint(pw):
    v = 0
    for i, d in enumerate(pw[::-1]):
        v += al.index(d) * (26 ** i)
    return v

def get_next(pw):
    npw = toint(pw) + 1
    return topw(npw)

def topw(pw):
    cpw = ''

    while pw:
        cpw += al[pw % 26]
        pw //= 26

    return cpw[::-1]

pw = 'xx'
for _ in range(5):
    print(pw)
    pw = get_next(pw)

while not isvalid(inp):
    inp = get_next(inp)

print(inp)
inp = get_next(inp)

while not isvalid(inp):
    inp = get_next(inp)

print(inp)
