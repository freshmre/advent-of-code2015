inp = [0]
reqs = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with open("inp.txt", "r") as f:
    while (l := f.readline().strip()):
        n, desc = l.split(': ', maxsplit=1)
        n = int(n[4:])

        curr = {}
        for prop in desc.split(', '):
            k, v = prop.split(': ')
            curr[k] = int(v)

        inp.append(curr)

def auntmatch(aunt):
    for k, v in aunt.items():
        if k in ['cats', 'trees']:
            if not v > reqs[k]:
                return False

        if k in ['pomeranians', 'goldfish']:
            if not v < reqs[k]:
                return False

        elif reqs[k] != v:
            return False
    return True

filtered_lst = list(filter(auntmatch, inp[1:]))
print(inp.index(filtered_lst[0]))

