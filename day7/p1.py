import re
from operator import rshift, lshift, and_, inv, or_
from functools import lru_cache
f = open("input.txt")
d = f.readlines()

op = re.compile("(?P<two>(\w+) ([RL]SHIFT|AND|OR) (\w+|\d+) -> (\w+))|(?P<not>NOT (\w+) -> (\w+))|(?P<store>(\w+|\d+) -> (\w+))")
two_op_funcs = {"RSHIFT":rshift, "LSHIFT":lshift, "AND":and_, "NOT":inv, "OR":or_}

class Op:
    def __init__(self, *args, **kwargs):
        self.inputs = [int(i) if i.isdigit() else i for i in args[:-1]]
        self.func = args[-1]
    def __repr__(self):
        return "in: " + str(self.inputs) + ", func:" + str(self.func)

ident = lambda x:x
nodes = {}
for l in d:
    o = op.search(l)
    optype = [k for k, v in o.groupdict().items() if v is not None][0]
    groups = o.groups()
    if optype == "two":
        in1 = groups[1]
        two_op = groups[2]
        in2 = groups[3]
        output = groups[4]
        func = two_op_funcs[two_op]
        fop = Op(in1,in2, func)
    elif optype == "not":
        not_in = groups[6]
        output = groups[7]
        fop = Op(not_in,inv)
    else:
        store_in = groups[9]
        output = groups[10]
        fop = Op(store_in,ident)
    nodes[output] = fop

@lru_cache(None)
def get_val(node_name):
    n_input = nodes[node_name]
    func_vals = [get_val(i) if type(i) is str else i for i in n_input.inputs ]
    return n_input.func(*func_vals) & 0xFFFF

print(get_val("a"))
