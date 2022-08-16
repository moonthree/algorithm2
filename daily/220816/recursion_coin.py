coin = [100, 70, 10]
n = int(input())

minimun = int(21e8)
def change(level, chan):
    global minimun
    if chan < 0:
        return
    if chan == 0:
        if level < minimun:
            minimun = level

    for i in range(3):
        change(level+1, chan-coin[i])

change(0, n)
print(minimun)