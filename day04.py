import hashlib

def check(key):
    return hashlib.md5(key.encode('utf-8')).hexdigest().startswith('000000')

key = 'yzbqklnj'

i = 0
while True:
    nkey = key + str(i)
    if (check(nkey)):
        print(i)
        break
    i += 1
