def bomb(y, x):
    idx = 0
    # 다이렉트 한바퀴
    while idx < 4:
        k = 1
        while True:
            ny = y + dy[idx] * k
            nx = x + dx[idx] * k
            if ny < 0 or nx < 0 or nx > 4 or ny > 4 or arr[ny][nx] == 3 or arr[ny][nx] == 1:
                idx += 1
                break
            arr[ny][nx] = 5
            k += 1


arr = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 1, 0],
    [0, 3, 0, 3, 0],
    [0, 1, 3, 1, 0],
    [0, 0, 0, 0, 0]
]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            bomb(i, j)
cnt = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 0:
            cnt += 1
print(cnt)
for i in range(5):
    for j in range(5):
        print(arr[i][j], end=' ')
    print()
