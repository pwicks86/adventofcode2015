import re
from collections import defaultdict
from itertools import permutations
f = open("input.txt")
d = f.readlines()

reg = re.compile(r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)")
lose_gain = defaultdict(dict)
for l in d:
    g = reg.match(l).groups()
    lose_gain[g[0]][g[3]] = (1 if g[1] == "gain" else -1) * int(g[2])

max_happy = 0
for p in permutations(lose_gain.keys()):
    happy = 0
    for i in range(len(p)):
        if i == 0:
            happy += lose_gain[p[i]][p[len(p)-1]]
            happy += lose_gain[p[i]][p[i+1]]
        elif i == len(p) - 1:
            happy += lose_gain[p[i]][p[0]]
            happy += lose_gain[p[i]][p[i-1]]
        else:
            happy += lose_gain[p[i]][p[i-1]]
            happy += lose_gain[p[i]][p[i+1]]

    max_happy = max(happy, max_happy)

print(max_happy)
