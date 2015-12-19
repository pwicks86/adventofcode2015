import re
f = open("input.txt")
d = f.readlines()

regexes = []
for l in d:
    if ("=" in l):
        s = list(map(str.strip,l.split(" => ")))
        regexes.append({
            "reg": re.compile("(?=({}))".format(s[0])),
            "len": len(s[0]),
            "rep": s[1]
        })
    else:
        if (len(l) > 1):
            rep_str = l

new_strs = set()
for reg in regexes:
    for m in reg["reg"].finditer(rep_str):
        start = m.start()
        new_str = rep_str[:start] + reg["rep"] + rep_str[start + reg["len"]:]
        new_strs.add(new_str)

print(len(new_strs))

