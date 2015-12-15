from itertools import combinations_with_replacement
import re
#f = open("test_input.txt")
f = open("input.txt")
d = f.readlines()

recipe = re.compile(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)")
stuff = {}

for l in d:
    print(l)
    g = recipe.match(l).groups()
    stuff[g[0]] =  {
        "capacity":int(g[1]),
        "durability":int(g[2]),
        "flavor":int(g[3]),
        "texture":int(g[4]),
        #"calories":int(g[5])
    }

ingredients = list(stuff.keys())
def get_cookie_score(cookie):
    global stuff
    score = 1
    for aspect in list(stuff.values())[0].keys():
        aspect_total = 0
        for ing, amount in cookie.items():
            ing_total = stuff[ing][aspect] * amount
            aspect_total += ing_total
        if aspect_total < 0:
            aspect_total = 0
        score *= aspect_total
    return score

teaspoons = 100
remaining = 100
top_score = 0
for combo in combinations_with_replacement(ingredients,100):
    cookie = {k:0 for k in ingredients}
    for i in combo:
        cookie[i] += 1
    score = get_cookie_score(cookie)
    top_score = max(top_score, score)

print(top_score)

