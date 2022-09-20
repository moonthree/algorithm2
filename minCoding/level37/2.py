from collections import deque

a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(b)]
y, x = map(int, input().split())
answer = 0
def bfs(sty, stx):
    global answer
    q = deque()
    q.append([sty, stx, 0])
    visited = [[0]*a for _ in range(b)]
    visited[sty][stx] = 1
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]
        answer = level
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > b-1 or dx > a-1 or visited[dy][dx] == 1 or arr[dy][dx] == 1:
                continue
            visited[dy][dx] = 1
            q.append([dy, dx, level+1])

bfs(y, x)
print(answer)