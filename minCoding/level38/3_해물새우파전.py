from collections import deque

def bfs(sty, stx, target):
    global flag
    q = deque()
    q.append([sty, stx, 0])

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    for i in range(4):
        while q:
            now = q.popleft()
            nowy, nowx, level = now[0], now[1], now[2]
            dy = nowy + directy[i]
            dx = nowx + directx[i]

            if dy < 0 or dx < 0 or dy > 6 or dx > 6:
                continue
            if arr[dy][dx] == target:
                flag = 1
            if level == target:
                break
            q.append([dy, dx, level+1])

arr = [list(map(int, input())) for _ in range(7)]
flag = 0
for i in range(7):
    for j in range(7):
        if arr[i][j] == 1:
            bfs(i, j, 1)
        if arr[i][j] == 2:
            bfs(i, j, 2)

if flag:
    print('fail')
else:
    print('pass')