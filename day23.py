inp = []

with open("inp.txt", "r") as f:
    while (l := f.readline().strip()):
        ins = l.replace(',', '').split()
        inp.append(ins)

def runins(registers, ins):
    op = ins[0]
    reg = ins[1]

    if op == 'hlf':
        registers[reg] //= 2

    elif op == 'tpl':
        registers[reg] *= 3

    elif op == 'inc':
        registers[reg] += 1

    elif op == 'jmp':
        return int(reg)

    elif op == 'jie':
        if (registers[reg] % 2) == 0:
            return int(ins[2])

    elif op == 'jio':
        if registers[reg] == 1:
            return int(ins[2])

    return 1

def interpreter(ins, astart=0):
    pc = 0
    registers = {'a': astart, 'b': 0}
    while pc < len(ins):
        pc += runins(registers, ins[pc])
    return registers['b']

print(interpreter(inp))
print(interpreter(inp, astart=1))
        


