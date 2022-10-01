# 4 6
# 탱크 = 0, 0에 위치
# 왕자 = 3, 5에 위치
# 탱크는 벽을 두 개 부실 수 있음

from collections import deque

def bfs(sty, stx, level, wall):
    global MIN

    q = deque()
    q.append([sty, stx, level, wall])

    visited = [[0] * 6 for _ in range(4)]
    visited[sty][stx] = 1

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    while q:
        now = q.popleft()
        print(now)
        nowy, nowx, level, wall = now[0], now[1], now[2], now[3]
        if nowy == 3 and nowx == 5:
            print(level)
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > 3 or dx > 5 or visited[dy][dx] == 1:
                continue
            if arr[dy][dx] == 1:
                wall += 1
            if wall < 3:
                visited[dy][dx] = level
                q.append([dy, dx, level+1, wall])
    for i in range(4):
        for j in range(6):
            print(visited[i][j], end=' ')
        print()

arr = [
    [0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 2]
]
bfs(0, 0, 0, 0)