import re

def calc_score(mults):
    p = 1

    for i in range(len(ings[0]) - 1):
        s = 0
        for n, m in enumerate(mults):
            s += m * ings[n][i]

        if s < 0:
            return 0
        p *= s

    return p

def calc_cals(mults):
    c = 0
    for i in range(len(mults)):
        c += ings[i][-1] * mults[i]
    return c


#ings = [[-1,-2,6,3,8], [2,3,-2,-1,3]]
#print(calc_score([44, 56]))

ings = []

with open("inp.txt", "r") as f:
    while l:=(f.readline()):
        match = re.findall(r'-?\d+',l)
        ings.append(list(map(int, match)))

print(calc_score([42, 52, 6, 0]))

best_score = 0
for w in range(101):
    for x in range(0, 101 - w):
        for y in range(0, 101 - w - x):
            for z in range(0, 101 - w - x - y):
                if calc_cals([w, x, y, z]) == 500 and (s:=calc_score([w, x, y, z])) > best_score:
                    best_i = (w, x, y, z)
                    best_score = s
    print(w)

print(best_score)
print(best_i)


    
