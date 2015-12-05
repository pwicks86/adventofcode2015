f = open("p1input.txt")
d = f.read()
floor = 0
i = 0
for c in d:
    i += 1
    if c == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print(i)
        break


