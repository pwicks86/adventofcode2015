from hashlib import md5
puz = "ckczppom"
n = 0

while True:
    m = md5()
    m.update((puz + str(n)).encode('ascii'))
    d = m.digest()
    if (sum(d[0:2]) == 0 and d[2] <= 15):
        print(d)
        print(n)
        break
    n+= 1



