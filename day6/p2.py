import re

f = open("input.txt")
d = f.readlines()

lights = [[0 for x in range(1000)] for x in range(1000)]
coords = re.compile("(\d+),(\d+) through (\d+),(\d+)")
for l in d:
    lcoords = coords.search(l)
    startx, starty, endx, endy = [int(c) for c in lcoords.groups()]
    for x in range(startx, endx + 1):
        for y in range(starty, endy+1):
            if l.startswith("toggle"):
                lights[x][y] = lights[x][y] + 2
            elif l.startswith("turn on"):
                lights[x][y] = lights[x][y] + 1
            else:
                lights[x][y] = max(0, lights[x][y] - 1)


t = 0
for r in range(len(lights)):
    t += sum(lights[r])

print(t)

