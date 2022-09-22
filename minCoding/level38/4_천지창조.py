from collections import deque

def bfs(sty, stx):
    global visited
    q = deque()
    q.append([sty, stx])
    visited[sty][stx] = True
    while q:
        now = q.popleft()
        nowy, nowx = now[0], now[1]
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > 7 or dx > 8:
                continue
            if visited[dy][dx] or arr[dy][dx] != '#':
                continue
            q.append([dy, dx])
            visited[dy][dx] = True
def bfs2(sty, stx):
    q = deque()
    q.append([sty, stx, 0])
    visited2 = [[False]*9 for _ in range(8)]
    visited2[sty][stx] = True
    MIN = 21e8
    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]
        if arr[nowy][nowx] == '#' and not visited[nowy][nowx]:
            MIN = min(MIN, level)
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > 7 or dx > 8:
                continue
            if visited2[dy][dx]:
                continue
            visited2[dy][dx] = True
            q.append([dy, dx, level+1])
    return MIN - 1


arr = [list(input()) for _ in range(8)]
visited = [[False]*9 for _ in range(8)]
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
flag = 0
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#':
            bfs(i, j)
            flag = 1
            break
    if flag:
        break

MINI = 21e8
for i in range(8):
    for j in range(9):
        if arr[i][j] == '#' and visited[i][j]:
            MINI = min(MINI, bfs2(i, j))

print(MINI)