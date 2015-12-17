from itertools import combinations
f = open("input.txt")
d = f.readlines()

nog = []
for l in d:
    nog.append(int(l))

combos = 0
for nog_len in range(len(nog)):
    for c in combinations(nog, nog_len):
        combo_sum = sum(c)
        if combo_sum == 150:
            combos += 1

print(combos)
