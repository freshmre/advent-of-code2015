from itertools import permutations

with open("inp.txt", "r") as f:
    inp = f.read().splitlines()

al = {}
for line in inp:
    source, _, dest, _, distance= line.split()

    if source not in al:
        al[source] = {}
    if dest not in al:
        al[dest] = {}
        
    al[source][dest] = int(distance)
    al[dest][source] = int(distance)

perms = permutations(al.keys())
min_dist = float('inf')
max_dist = 0

for path in perms:
    cur = sum(al[path[i]][path[i+1]] for i in range(len(path) - 1))
    min_dist = min(min_dist, cur)
    max_dist = max(max_dist, cur)


print("shortest: %d" % min_dist)
print("longest: %d" % max_dist)
