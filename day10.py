with open("inp.txt", "r") as f:
    inp = f.read().strip()

def round(num):
    num += '_'
    res = ''
    count = 1
    for i in range(len(num) - 1):
        if num[i] == num[i+1]:
            count += 1
        else:
            res += str(count) + str(num[i])
            count = 1
    return res

n = inp
for _ in range(40):
    n = round(n)

print(len(n))

for _ in range(10):
    n = round(n)

print(len(n))
