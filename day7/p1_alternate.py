# Alternate solution for day 7 inspired by this post (https://www.reddit.com/r/adventofcode/comments/3vr4m4/day_7_solutions/cxq07ki) on reddit
import re
f = open("input.txt")
d = f.read()
d = d.replace("RSHIFT", ">>")
d = d.replace("LSHIFT", "<<")
d = d.replace("NOT", "~")
d = d.replace("OR", "|")
d = d.replace("AND", "&")
d = d.replace("->", "")
d = d.replace("as", "as_")
d = d.replace("if", "if_")
d = d.replace("in", "in_")
d = d.replace("is", "is_")
def s(l):
    split_l = l.rsplit(" ", 1)
    return split_l[1] +" = " + split_l[0]

ll = [s(l) for l in d.split("\n") if len(l) > 0]
ll = sorted(ll, key = lambda i:(len(re.split("\s|_", i)[0]),i.split(" ")[0]))
ll.insert(len(ll), ll.pop(0))
x = "\n".join(ll)
exec(x)
print(a)
