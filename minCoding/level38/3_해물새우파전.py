from collections import deque

def bfs(sty, stx, target, goal):
    global flag, arr
    q = deque()
    q.append([sty, stx, 1])

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    for i in range(4):
        while q:
            now = q.popleft()
            nowy, nowx, level = now[0], now[1], now[2]
            print(now)
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if level == goal:
                break
            if dy < 0 or dx < 0 or dy > 6 or dx > 6:
                continue
            if arr[dy][dx] == target:
                flag = 1
            arr[dy][dx] = 2
            q.append([dy, dx, level+1])

arr = [list(map(int, input())) for _ in range(7)]
flag = 0
for i in range(7):
    for j in range(7):
        if arr[i][j] == 1:
            bfs(i, j, 1, 3)
        elif arr[i][j] == 2:
            bfs(i, j, 2, 4)

if flag:
    print('fail')
else:
    print('pass')

# 0001000
# 0000000
# 0000000
# 0000000
# 0000000
# 0000000
# 0000000
for i in range(7):
    for j in range(7):
        print(arr[i][j], end=' ')
    print()