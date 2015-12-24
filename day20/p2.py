from itertools import count
from math import sqrt
from collections import Counter
puz_input = 33100000

factor_count = Counter()
def get_factors(n):
    global factor_count
    def check_count(factor, flist):
        if factor_count[factor] > 50:
            pass
        else:
            factor_count[factor] += 1
            flist.add(factor)
    root = sqrt(n)
    i = 2
    factors = set([1, n])
    while i <= root:
        if n % i == 0:
            check_count(i, factors)
            div = (n//i)
            check_count(div, factors)
        i += 1
    return factors

for house in count(1,1):
    x = sum([ i * 11 for i in get_factors(house)])
    if x >= puz_input:
        print(house)
        break


