from itertools import combinations, chain
from collections import defaultdict
f = open("input.txt")
d = f.readlines()
boss_dict = {}
for l in d:
    s = l.split(":")
    if ("Hit" in s[0]):
        boss_dict["HP"] = int(s[1])
    else:
        boss_dict[s[0]] = int(s[1])

shop_txt = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""
shop = defaultdict(list)
for l in shop_txt.splitlines():
    if ":" in l:
        cur_type = l.split(":")[0]
    elif len(l) > 1:
        attr = l.split()
        shop[cur_type].append(dict(Name=attr[0], Cost = int(attr[1]), Damage = int(attr[2]), Armor = int(attr[3])))

def do_battle(weapon, armor, rings):
    global boss
    me = dict(HP=100, Damage= 0, Armor = 0)
    boss = dict(boss_dict)
    cost = weapon["Cost"]
    me["Damage"] += weapon["Damage"]
    if armor:
        me["Armor"] += armor["Armor"]
        cost += armor["Cost"]
    for r in rings:
        me["Damage"] += r["Damage"]
        me["Armor"] += r["Armor"]
        cost += r["Cost"]

    while me["HP"] > 0:
        boss["HP"] -= max(1,me["Damage"] - boss["Armor"])
        if boss["HP"] <= 0:
            break
        me["HP"] -= max(1,boss["Damage"] - me["Armor"])
    return (True if me["HP"] > 0 else False, cost)


battle_results = []
x = 0
for weapon in shop["Weapons"]:
    for armor in (shop["Armor"]  + [None]):
        for rings in chain(combinations(shop["Rings"], 2), combinations(shop["Rings"],1),combinations(shop["Rings"],0)):
            battle_results.append(do_battle(weapon, armor, rings))

losses = [b for b in battle_results if not b[0]]
losses.sort(key = lambda l: l[1])
print(losses[-1][1])
