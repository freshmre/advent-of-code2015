with open("inp.txt", "r") as f:
    inp = f.read().strip()

v = 0
found = False
for i, char in enumerate(inp):
    if char == '(':
        v += 1
    elif char == ')':
        v -= 1
    if not found and v < 0:
        found = True
        print(i)

print(v)