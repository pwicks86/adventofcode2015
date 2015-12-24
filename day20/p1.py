from itertools import count
from math import sqrt
puz_input = 33100000

def get_factors(n):
    root = sqrt(n)
    i = 2
    factors = set([1, n])
    while i <= root:
        if n % i == 0:
            factors.add(i)
            div = (n//i)
            if i != div :
                factors.add(div)
        i += 1
    return factors

for house in count(1,1):
    x = sum([ i * 10 for i in get_factors(house)])
    if x >= puz_input:
        print(house)
        break

