from math import inf
from itertools import permutations
import re

happiness_map = {}
names = set()

with open("inp.txt", "r") as f:
    while (l := f.readline().strip()):
        pattern = r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.'
        vals = re.match(pattern, l).groups()

        happiness_delta = int(vals[2])
        if vals[1] == 'lose':
            happiness_delta *= -1

        pair = (vals[0], vals[-1])

        happiness_map[pair] = happiness_delta

        names.add(vals[0])

def calc_happiness(lst):
    score, l = 0, len(lst)
    for i in range(l):
        p1, p2 = lst[i], lst[(i+1) % l]
        if 'Me' not in (p1, p2):
            score += happiness_map[(p1, p2)]
            score += happiness_map[(p2, p1)]
    return score


max_hap = -inf
perms = permutations(names)

for p in perms:
    if (score := calc_happiness(p)) > max_hap:
        max_hap = score

print(max_hap)


names.add('Me')
max_hap = -inf
perms = permutations(names)

for p in perms:
    if (score := calc_happiness(p)) > max_hap:
        max_hap = score

print(max_hap)
