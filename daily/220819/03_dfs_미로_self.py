arr = [[0, 0, 0, 0],
       [1, 0, 1, 0],
       [0, 0, 1, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 0]
       ]

visit = [[0] * 4 for _ in range(5)]
miro = []
miro_idx = []

def dfs(y, x, cnt, start_y, start_x):
    if y == 3 and x == 3:
        miro.append(cnt)
        miro_idx.append([start_y, start_x])
        return
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy > 4 or dx > 3:
            continue
        if visit[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        visit[dy][dx] = 1
        dfs(dy, dx, cnt + 1, start_y, start_x)
        visit[dy][dx] = 0


for i in range(4):
    for j in range(5):
        visit[j][i] = 1
        dfs(j, i, 0, j, i)
        visit[j][i] = 0
