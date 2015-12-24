f = open("input.txt")
d = f.readlines()

replacements = []
for l in d:
    if ("=" in l):
        s = list(map(str.strip,l.split(" => ")))
        replacements.append(s)
    elif (len(l) > 1):
        rep_str = l

replacements.sort(key=lambda x:len(x[1]))
replacements = list(reversed(replacements))
step = 0
seen_states = set()
search_queue = [(step, rep_str[:-1])]
while(True):
    cur = search_queue.pop(0)
    if (cur[1] == "e"):
        print(cur[0])
        break
    for rep in replacements:
        if rep[1] in cur[1]:
            new_str = cur[1].replace(rep[1], rep[0], 1)
            if (new_str not in seen_states):
                seen_states.add(new_str)
            else:
                continue
            search_queue.insert(0, (cur[0] + 1, new_str))
            break

