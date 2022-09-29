# 벽 = 3
# 폭탄 = 1

def bomb(y, x):
    visited = [[False]*w for _ in range(h)]
    visited[y][x] = True
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        flag = 1
        while flag:
            if dy < 0 or dx < 0 or dy > 4 or dx > 4 or visited[dy][dx] or arr[dy][dx] == 3:
                flag = 0
                continue
            arr2[dy][dx] = 1
            visited[dy][dx] = True
            dy += directy[i]
            dx += directx[i]


arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 3, 0, 3, 0],
    [0, 1, 3, 1, 0],
    [0, 0, 0, 0, 0]
]
arr2 = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 3, 0, 3, 0],
    [0, 1, 3, 1, 0],
    [0, 0, 0, 0, 0]
]
h = len(arr)
w = len(arr[0])

for i in range(h):
    for j in range(w):
        if arr[i][j] == 1:
            bomb(i, j)
for i in range(h):
    for j in range(w):
        print(arr2[i][j], end=' ')
    print()
cnt = 0
for i in arr2:
    cnt += i.count(0)

print(cnt)