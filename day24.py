from functools import reduce
from itertools import combinations
from operator import mul

with open("inp.txt", "r") as f:
    inp = list(map(int, f.read().split()))

size = 4
weight = sum(inp) // size

for i in range(len(inp)):
    groups = [reduce(mul, c) for c in combinations(inp, i) if sum(c) == weight]
    if groups:
        print(min(groups))
        break


