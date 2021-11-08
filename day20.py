from itertools import combinations
from functools import reduce
from operator import mul

def getdivs(n):
    i = 2
    divs = []
    while (i * i) <= n:
        if (n % i) == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(n)
    return divs

def getgifts(n, new=0):
    mult = 10
    divs = getdivs(n)
    alldivs = set([1]) 
    for i in range(1, len(divs) + 1):
        for comb in combinations(divs, r=i):
            alldivs.add(reduce(mul, comb))

    if new:
        alldivs = filter(lambda k: (n // k) <= 50, alldivs)
        mult = 11

    return sum(alldivs) * mult

target = 36000000

p1 = 1
while (n := getgifts(p1)) < target:
    p1 += 1

p2 = 1
while (n := getgifts(p2, new=True)) < target:
    p2 += 1

print(p1)
print(p2)
