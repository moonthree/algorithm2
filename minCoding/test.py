import random


def r(n):
    global c, v
    c += 1
    v[n] = 1
    print(n, end=' ')
    if c == 7:
        return
    while 1:
        p = random.randrange(1, 46)
        if v[p] != 1:
            break
    r(p)


c = 0
v = [0] * 46
print('이번주 로또 번호는')
r(random.randrange(1, 46))
