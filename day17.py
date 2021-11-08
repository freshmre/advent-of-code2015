from functools import reduce
from itertools import combinations, permutations

with open("inp.txt", "r") as f:
    inp = list(map(int, f.read().splitlines()))

target = 150
combs = [combinations(inp, r=i+1) for i in range(len(inp))]
valid_combs = list(filter(lambda l: sum(l) == target, 
    (lst for gen in combs for lst in gen)))

shortest = len(reduce(lambda x, y: x if len(x) < len(y) else y, valid_combs))
n_ways = len(list(filter(lambda x: len(x) == shortest, valid_combs)))

print(f"combinations of containers: {len(valid_combs)}")
print(f"arrangements of containers: {n_ways}")
