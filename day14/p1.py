from math import modf
import re
f = open("input.txt")
d = f.readlines()

deer_re  = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
deers = {}
for l in d:
    g = deer_re.match(l).groups()
    deers[g[0]] = {"speed":int(g[1]), "time":int(g[2]), "rest":int(g[3])}

race_time = 2503
max_dist = 0
for name,deer in deers.items():
    cycle_time = deer["time"] + deer["rest"]
    partial, full = modf(race_time/cycle_time)
    per_cycle_dist = deer["speed"] * deer["time"]
    total_dist = per_cycle_dist * full
    remaining_time = min((partial * cycle_time), deer["time"])
    if (remaining_time > 0):
        total_dist += remaining_time * deer["speed"]
    max_dist = max(total_dist, max_dist)

print(max_dist)

