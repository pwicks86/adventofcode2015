f = open("input.txt")
d = f.readlines()
nice = 0

def check_split(word):
    for i in range(len(word) - 3):
        if word[i] == word[i+2]:
            return True
    return False

def check_pair(word):
    for i in range(len(word) - 2):
        if word[i:i+2] in word[i+2:]:
            return True
    return False

for l in d:
    if not check_split(l):
        continue
    if check_pair(l):
        nice += 1

print(nice)
