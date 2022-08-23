t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visit = [['0']*n for _ in range(n)]

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    mini = int(21e8)
    def miro(y, x, move):
        global mini
        if arr[y][x] == '3':
            if move - 1 < mini:
                mini = move - 1
            return

        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if visit[dy][dx] == '1':
                continue
            if arr[dy][dx] == '1' or arr[dy][dx] == '2':
                continue
            visit[y][x] = '1'
            miro(dy, dx, move+1)
            visit[y][x] = '0'

    flag = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                miro(i, j, 0)
                flag = 1
        if flag:
            break

    if mini == int(21e8):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {mini}')


