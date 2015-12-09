from collections import defaultdict
from itertools import permutations
import re
f = open("input.txt")
d = f.readlines()

line_re = re.compile(r"(\w+) to (\w+) = (\d+)")
distances = defaultdict(dict)

for l in d:
    l_groups = line_re.match(l).groups()
    dist = int(l_groups[2])
    distances[l_groups[0]][l_groups[1]] = dist
    distances[l_groups[1]][l_groups[0]] = dist

cities = distances.keys()
min_combo = None
min_dist = 2**32
for combo in permutations(cities, len(cities)):
    cur_dist = 0
    for i in range(len(combo) -1):
        cur_city = combo[i]
        next_city = combo[i+1]
        cur_dist += distances[cur_city][next_city]
    if (cur_dist < min_dist):
        min_dist = cur_dist
        min_combo = combo

print(min_combo)
print(min_dist)

