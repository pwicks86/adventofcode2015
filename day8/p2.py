import re
f = open("input.txt")
d = f.readlines()
code_len = 0
char_len = 0

for l in d:
    l = l.strip()
    code_len += len(l)
    l = l.replace("\\","\\\\")
    l = re.sub(r"\"", r"\"", l)
    char_len += len(l) + 2

print(char_len - code_len)
