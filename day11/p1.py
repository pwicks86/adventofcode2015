from itertools import islice

puz_input = list("hxbxwxba")

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def increment(pw):
    for i in range(len(pw) -1, -1, -1):
        if (pw[i] == "z"):
            pw[i] = "a"
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break
    return pw

def increasing_straight(pw):
    for triplet in window(pw,3):
        t_ord = [ord(t) for t in triplet]
        if (t_ord[0] + 1 == t_ord[1] and t_ord[1] + 1 == t_ord[2]):
            return True
    return False

def contains_iol(pw):
    return "i" in pw or "o" in pw or "l" in pw

def has_pairs(pw):
    pair_set = set([t for t in window(pw,2) if t[0] == t[1]])
    return len(pair_set) >= 2

p = puz_input
while True:
    p = increment(p)
    if contains_iol(p):
        continue
    if not increasing_straight(p):
        continue
    if not has_pairs(p):
        continue
    print("".join(p))
    break
