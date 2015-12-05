f = open("p1input.txt")
d = f.read()
floor = 0
for c in d:
    if c == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
