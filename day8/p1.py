import re
f = open("input.txt")
d = f.readlines()
code_len = 0
char_len = 0

def fixer(m):
    try:
        return chr(int(m.group()[-2:],16))
    except:
        return m.group()

for l in d:
    l = l.strip()
    code_len += len(l)
    l = re.sub(r"^(\\)\\x\w{2}",fixer,l)
    l = "\"\"" + l + "\"\""
    char_len += eval("len(" + l + ")")

print(code_len - char_len)
