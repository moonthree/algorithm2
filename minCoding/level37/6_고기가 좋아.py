from collections import deque

def bfs(sty, stx):
    global cnt
    q = deque()
    q.append([sty, stx])

    visited = [[False]*6 for _ in range(4)]
    visited[sty][stx] = True

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        nowy, nowx = now[0], now[1]
        if arr[nowy][nowx] == 2:
            cnt += 1

        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > 3 or dx > 5:
                continue
            if visited[dy][dx] or arr[dy][dx] == 1:
                continue
            visited[dy][dx] = 1
            q.append([dy, dx])

arr = [list(map(int, input().split())) for _ in range(4)]
cnt = 0
bfs(0, 0)
print(cnt)