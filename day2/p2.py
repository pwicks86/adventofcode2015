from itertools import combinations
from operator import mul
from functools import reduce

f = open("input.txt")
d = f.readlines()
total = 0
for p in d:
    sides = [int(n) for n in p.split("x")]
    sides.sort()
    total += (sides[0] + sides[1]) * 2
    total += reduce(mul,sides, 1)


print(total)
