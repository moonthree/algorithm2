from collections import deque

def bfs(sty, stx, level, cnt):
    q = deque()
    q.append([sty, stx, level, cnt])

    visited = [[False]*x for _ in range(y)]
    visited[sty][stx] = True

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        nowy, nowx, level, cnt = now[0], now[1], now[2], now[3]

        if not cnt:
            if arr[nowy][nowx] == 'C':
                bfs(nowy, nowx, level, cnt+1)
        else:
            if arr[nowy][nowx] == 'D':
                print(level)

        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > y-1 or dx > x-1:
                continue
            if visited[dy][dx] or arr[dy][dx] == 'x':
                continue
            visited[dy][dx] = 1
            q.append([dy, dx, level+1, cnt])

y, x = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(y)]

for i in range(y):
    for j in range(x):
        if arr[i][j] == 'S':
            bfs(i, j, 0, 0)
