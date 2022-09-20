from collections import deque

def bfs(sty, stx):
    q = deque()
    q.append([sty, stx, 0])

    visited = [[False]*4 for _ in range(4)]
    visited[sty][stx] = True

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]

        if nowy == ey and nowx == ex:
            print(f'{level}회')

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > 3 or dx > 3:
                continue
            if arr[dy][dx] == 1 or visited[dy][dx]:
                continue
            visited[dy][dx] = 1
            q.append([dy, dx, level+1])


arr = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]

y, x = map(int, input().split())
ey, ex = map(int, input().split())

bfs(y, x)