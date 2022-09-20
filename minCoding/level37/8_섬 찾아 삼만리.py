from collections import deque


def bfs(sty, stx):
    global visited
    q = deque()
    q.append([sty, stx])

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        nowy, nowx = now[0], now[1]

        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx

            if dy < 0 or dx < 0 or dy > y-1 or dx > x-1:
                continue
            if arr[dy][dx] == 0 or visited[dy][dx]:
                continue
            visited[dy][dx] = True
            q.append([dy, dx])


y, x = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(y)]
visited = [[False]*x for _ in range(y)]
cnt = 0
for i in range(y):
    for j in range(x):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)