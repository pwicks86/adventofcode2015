from itertools import combinations
from operator import mul

f = open("input.txt")
d = f.readlines()
total = 0
for p in d:
    sides = [int(n) for n in p.split("x")]
    combos = list(combinations(sides, 2))
    areas = [ mul(*a) for a in combos]
    areas.sort()
    total += areas[0]
    total += sum([2*a for a in areas])

print(total)
