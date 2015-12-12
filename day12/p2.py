import re
import json
f = open("input.txt")
d = f.read()

def no_red(decoded):
    if "red" in decoded.values():
        return None
    else:
        return decoded

d = json.dumps(json.loads(d, object_hook=no_red))

s = 0
for n in re.findall(r"(-?\d+)", d):
    s+= int(n)
print(s)
