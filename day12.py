import json

with open("inp.txt", "r") as f:
    inp = f.read()

def nored(obj, allow_red=1):
    total = 0
    if type(obj) == int:
        total = obj

    elif type(obj) == list:
        for sub in obj:
            total += nored(sub, allow_red)

    elif type(obj) == dict:
        if allow_red or 'red' not in obj.values():
            for sub in obj.values():
                total += nored(sub, allow_red)

    return total

inp = (json.loads(inp))

print(nored(inp))
print(nored(inp, 0))
