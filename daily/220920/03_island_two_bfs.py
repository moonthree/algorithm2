from collections import deque


def bfs(sty, stx):
    q = deque()
    q.append([sty, stx])
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    size = 1

    while q:
        now = q.popleft()
        nowy, nowx = now[0], now[1]
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > 4 or dx > 4 or used[dy][dx] == 1:
                continue
            if arr[dy][dx] == 1:
                used[dy][dx] = 1
                q.append([dy, dx])
                size += 1
    return size


arr = [[1, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 0, 1, 1]]
used = [[0] * 5 for _ in range(5)]
cnt = 0
MAX = -21e8
MIN = 21e8
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1 and used[i][j] == 0:
            used[i][j] = 1
            cnt += 1
            a = bfs(i, j)
            MAX = max(a, MAX)
            MIN = min(a, MIN)

print(cnt, MIN, MAX)

