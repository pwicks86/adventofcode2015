from operator import mul
from functools import reduce
from itertools import combinations
from itertools import takewhile
f = open("input.txt")

presents = list(map(int,f.readlines()))
num_presents = len(presents)
total_weight = sum(presents)
balance_weight = total_weight//3
candidates = []

for i in range(10):
    for combo in combinations(presents,i):
        combo_sum = sum(combo)
        if combo_sum == balance_weight:
            candidates.append(list(combo))
candidates.sort(key=lambda i: len(i))
shortest_len = len(candidates[0])

candidates = takewhile(lambda i: len(i) == shortest_len, candidates)
quantums = [reduce(mul,c,1) for c in candidates]
quantums.sort()
print(quantums[0])
