f = open("input.txt")
d = f.readlines()
nice = 0
bad_strings = ["ab", "cd", "pq", "xy"]
def check_bad(word):
    for s in bad_strings:
        if s in word:
            return True
    return False

def check_twice(word):
    for i in range(len(word) -2 ):
        if word[i] == word[i+1]:
            return True
    return False

for l in d:
    if check_bad(l):
        continue
    vowels = list(filter(lambda i: i in "aeiou", l))
    if len(vowels) < 3:
        continue
    if check_twice(l):
        nice += 1

print(nice)
