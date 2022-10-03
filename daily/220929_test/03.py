def water_bomb(y, x):
    global arr, visited
    idx = 0
    visited[y][x] = True
    while idx < 4:
        didx = 1
        while True:
            dy = directy[idx]*didx + y
            dx = directx[idx]*didx + x
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1 or arr[dy][dx] == 3 or arr[dy][dx] == 1:
                break
            arr[dy][dx] = 2
            visited[dy][dx] = True
            didx += 1
        idx += 1

arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 3, 1, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 0, 0, 0, 0]
]

n = len(arr)
visited = [[False]*n for _ in range(n)]
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            water_bomb(i, j)
cnt = 0
for i in arr:
    cnt += i.count(0)

print(cnt)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()