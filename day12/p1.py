import re
f = open("input.txt")
d = f.read()

s = 0
for n in re.findall(r"(-?\d+)", d):
    s+= int(n)
print(s)
