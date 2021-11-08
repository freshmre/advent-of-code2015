with open("inp.txt", "r") as f:
    inp = f.read().splitlines()

def parseline(line):
    new_str = ""
    i = 1
    while i < (len(line) - 1):
        c = line[i]

        if c != '\\':
            new_str += line[i]
            i += 1
            continue
        
        nc = line[i+1]
        if nc == '\\' or nc == '"':
            new_str += nc
            i += 2
            continue

        nnc = line[i+2:i+4]
        new_str += chr(int(nnc, 16))
        i += 4
    return new_str

def lenencode(line):
    return len(line) + 2 + line.count('"') + line.count("\\")
    
parsed = [parseline(line) for line in inp]
total_diff = sum(len(inp[i]) - len(parsed[i]) for i in range(len(inp)))
total_encode = sum(lenencode(inp[i]) - len(inp[i]) for i in range(len(inp)))

# total_diff = 0
# for i in range(len(inp)):
#     li, lp = len(inp[i]), len(parsed[i])
#     print(li, lp)
#     total_diff += li - lp

print(total_diff)
print(total_encode)

# t = r'"hello\x41"'
# n = parseline(t)
# print(n)

