from math import modf
from collections import defaultdict
from itertools import cycle, islice
import re

f = open("input.txt")
d = f.readlines()

deer_re  = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
deers = {}
for l in d:
    g = deer_re.match(l).groups()
    deers[g[0]] = {"speed":int(g[1]), "time":int(g[2]), "rest":int(g[3])}

race_time = 2503
points = defaultdict(int)
dists = defaultdict(int)
racing = defaultdict(list)

for name, deer in deers.items():
    rcycle = [1] * deer["time"]
    rcycle.extend([0] * deer["rest"])
    racing[name] = list(islice(cycle(rcycle),race_time+1))

points = defaultdict(int)
for s in range(race_time + 1):
    for name, deer in deers.items():
        dists[name] += racing[name][s] * deer["speed"]
    cur_lead = max(dists.values())
    for name, dist in dists.items():
        if dist >= cur_lead:
            points[name] += 1

print(points)
