from collections import deque

arr = [list(map(int, input().split())) for _ in range(4)]
answer = 1
def bfs(sty, stx):
    global answer
    q = deque()
    q.append([sty, stx, 1])
    directy = [0, 0, -1, 1]
    directx = [-1, 1, 0, 0]
    visited = [[0]*4 for _ in range(4)]
    visited[sty][stx] = 1

    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]

            if dy < 0 or dx < 0 or dy > 3 or dx > 3 or visited[dy][dx] == 1:
                continue
            if arr[dy][dx] == 0:
                continue
            q.append([dy, dx, level+1])
            visited[dy][dx] = 1
            answer += 1

bfs(0, 0)
print(answer)