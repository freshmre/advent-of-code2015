MAX_INT = 65535

with open("inp.txt", "r") as f:
    inp = f.read().splitlines()

# component map
def make_map():
    global wires, inp

    wires = {}
    for line in inp:
        equation, out = line.split(' -> ')
        ops = equation.split()
        if len(ops) == 3:
            ops[0], ops[1] = ops[1], ops[0]

        wires[out] = ops

ops = {
    'AND': (lambda a, b: a & b),
    'OR': (lambda a, b: a | b),
    'RSHIFT': (lambda a, b: a >> b),
    'LSHIFT': (lambda a, b: (a << b) & MAX_INT),
    'NOT': (lambda a, b: MAX_INT - a),
}

cache = {}

def operate(wire: str):
    eq = wires[wire]
    if wire in cache:
        return cache[wire]

    if eq[0].isdigit():
        v = int(eq[0])
        cache[wire] = v
        return v

    if len(eq) == 1:
        return operate(eq[0])

    if eq[1].isdigit():
        a = int(eq[1])
    else:
        a = operate(eq[1])

    b = 0

    if len(eq) == 3:
        if eq[2].isdigit():
            b = int(eq[2])
        else:
            b = operate(eq[2])

    res = ops[eq[0]](a, b)
    cache[wire] = res
    return res

make_map()

# print(wires)
p1 = operate('a')
cache.clear()

wires['b'] = [str(p1)]
p2 = operate('a')


print(p1)
print(p2)

# exec 

"""
a: b
b: c
c: d
d: '10'
"""