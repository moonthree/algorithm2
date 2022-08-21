maps = [['_' for _ in range(5)] for _ in range(4)]

# 00 01 02
# 10 11 12
# 20 21 22

directy = [-1, -1, -1, 0, 1, 1, 1, 0]
directx = [-1, 0, 1, 1, 1, 0, -1, -1]

def explode(y, x):
    for i in range(8):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dy > 3 or dx < 0 or dx > 4:
            continue
        if maps[dy][dx] == '_':
            maps[dy][dx] = maps[dy][dx].replace('_', '#')


bomb = []
for _ in range(2):
    bomb.append(list(map(int, input().split())))

for i in bomb:
    explode(i[0], i[1])

for i in range(len(maps)):
    for j in range(len(maps[i])):
        print(maps[i][j], end=' ')
    print()