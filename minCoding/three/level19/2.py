maps = [[3, 3, 5, 3, 1], [2, 2, 4, 2, 6], [4, 9, 2, 3, 4], [1, 1, 1, 1, 1], [3, 3, 5, 9, 2]]

# 00 01 02
# 10 11 12
# 20 21 22

# 00 02 20 22

directy = [-1, -1, 1, 1]
directx = [-1, 1, -1, 1]

Max = int(-21e8)
maxy = 0
maxx = 0

def getSum(y, x):
    sums = 0
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dy > 4 or dx < 0 or dx > 4:
            continue
        sums += maps[dy][dx]
    return sums

for i in range(5):
    for j in range(5):
        result = getSum(i, j)
        if result > Max:
            Max = result
            maxy = i
            maxx = j

print(maxy, maxx)