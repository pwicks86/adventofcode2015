from hashlib import md5
puz = "ckczppom"
n = 0

while True:
    m = md5()
    m.update((puz + str(n)).encode('ascii'))
    d = m.digest()
    if (sum(d[0:3]) == 0):
        print(d)
        print(n)
        break
    n+= 1



