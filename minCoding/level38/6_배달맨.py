from collections import deque

def bfs(sty, stx, target, level):
    global answer
    q = deque()
    q.append([sty, stx, target, level])

    visited = [[False]*x for _ in range(y)]
    visited[sty][stx] = True

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    while q:
        now = q.popleft()
        nowy, nowx, target, level = now[0], now[1], now[2], now[3]
        if target == 4 and arr[nowy][nowx] == str(target):
            answer.append(level)
        if arr[nowy][nowx] == str(target):
            bfs(nowy, nowx, target+1, level)

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]

            if dy < 0 or dx < 0 or dy > y-1 or dx > x-1:
                continue
            if visited[dy][dx] or arr[dy][dx] == '#':
                continue
            visited[dy][dx] = True
            q.append([dy, dx, target, level+1])


y, x = map(int, input().split())
arr = [list(input()) for _ in range(y)]
answer = []
bfs(0, 0, 1, 0)
print(f'{min(answer)}회')