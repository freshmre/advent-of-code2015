with open("inp.txt", "r") as f:
    inp = f.read().splitlines()

def check(name):
    return pair(name) and twice(name)

def pair(name):
    for i in range(len(name) - 1):
        sub = name[i:i+2]
        # print(sub)
        news = name[:i] + '__' + name[i+2:]
        # print(news)
        if news.count(sub) >= 1:
            print(name, sub)
            return True
    return False

def twice(name):
    for i in range(len(name)-2):
        if name[i] == name[i+2]:
            # print(name[i:i+3])
            return True
    return False

# print(check('qjhvhtzxzqqjkmpb'))
# print(check('xxyxx'))
# print(pair('uurcxstgmygtbstg'))
# print(twice('ieodomkazucvgmuy'))
# print(pair('abcdefeghi'))

total = 0
for name in inp:
    total += check(name)

print(total)