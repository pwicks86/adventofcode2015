import re
f = open("input.txt")
d = f.readlines()

sue_reg = re.compile(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")
sues = []
input2 = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

for l in d:
    g = sue_reg.match(l).groups()
    sue_dict = {"num":g[0], g[1]:int(g[2]), g[3]:int(g[4]),g[5]:int(g[6])}
    sues.append(sue_dict)

for cond,val in input2.items():
    sues = [sue for sue in sues if cond not in sue or (cond in ["cats", "trees"] and sue[cond] > val) or (cond in ["pomeranians", "goldfish"] and sue[cond] < val) or sue[cond] == val]

print(sues[0]["num"])
