from collections import deque
def bfs(sty, stx):
    q = deque()
    q.append([sty, stx, 0])
    visited = [[False]*n for _ in range(n)]
    visited[sty][stx] = True
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        nowy, nowx, total = now[0], now[1], now[2]
        print(nowy, nowx, total)
        if nowy == n-1 and nowx == n-1:
            print(total)

        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if visited[dy][dx]:
                continue
            visited[dy][dx] = True
            q.append([dy, dx, total+arr[dy][dx]])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    bfs(0, 0)
