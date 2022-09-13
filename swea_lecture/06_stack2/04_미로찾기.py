t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visit = [['0']*n for _ in range(n)]
    miro = '0'

    def dfs(y, x, move):
        global miro
        if move > 1000:
            return
        if arr[y][x] == '3':
            miro = '1'
            return

        direct_y = [-1, 1, 0, 0]
        direct_x = [0, 0, -1, 1]
        for i in range(4):
            dy = y + direct_y[i]
            dx = x + direct_x[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if visit[dy][dx] == '1':
                continue
            if arr[dy][dx] == '1' or arr[dy][dx] == '2':
                continue
            visit[y][x] = '1'
            dfs(dy, dx, move+1)
            visit[y][x] = '0'

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                dfs(i, j, 0)
                break
    if miro == '1':
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')