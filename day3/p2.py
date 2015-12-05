from collections import defaultdict
f = open("input.txt")
d = f.read()
houses = defaultdict(int,{(0,0):1})
santa =  [0,0]
robo_santa =  [0,0]
cur = santa
for c in d:
    if (cur is santa):
        cur = robo_santa
    else:
        cur = santa
    if c == "<":
        cur[0] -= 1
    if c == ">":
        cur[0] += 1
    if c == "v":
        cur[1] += 1
    if c == "^":
        cur[1] -= 1
    houses[tuple(cur)]+=1

print(len(houses.keys()))
