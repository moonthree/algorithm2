arr = [[0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1],
       [0, 0, 0, 0, 0]]

visit = [[0] * 5 for _ in range(4)]

move_list = []
move = int(21e8)

def dfs(y, x, cnt):
    global move
    if y == 1 and x == 3:
        move_list.append(cnt)
        if cnt < move:
            move = cnt
        return

    direct_y = [-1, 1, 0, 0]
    direct_x = [0, 0, -1, 1]
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 4:
            continue
        if visit[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        visit[y][x] = 1
        dfs(dy, dx, cnt+1)
        visit[y][x] = 0


visit[0][0] = 1
dfs(0, 0, 0)
visit[0][0] = 0
print(move)
print(move_list)