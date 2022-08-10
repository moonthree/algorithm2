maps = [[3, 5, 1], [3, 8, 1], [1, 1, 5]]

bitarray = [list(map(int, input().split()))for _ in range(2)]
# 1 1
# 1 0

MAX = int(-21e8)
maxy = 0
maxx = 0

def getSum (y, x):
    sums = 0
    for i in range(2):
        for j in range(2):
            if i+y < 0 or i+y > 2 or j+x < 0 or j+x > 2:
                continue
            sums += maps[i+y][j+x]*bitarray[i][j]

    return sums

for i in range(len(maps)):
    for j in range(len(maps[i])):
        result = getSum(i, j)
        if result > MAX:
            MAX = result
            maxy = i
            maxx = j

print(f'({maxy},{maxx})')