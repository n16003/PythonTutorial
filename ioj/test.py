import string

count = {x: 0 for x in string.ascii_lowercase}
lines = ""

while True:
    try:
        lines += input().lower()
    except EOFError:
        break

for c in lines:
    if 'a' <= c <= 'z':
        count[c] += 1

for key in string.ascii_lowercase:
    print("{0} : {1}".format(key, count[key]))