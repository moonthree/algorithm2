arr = [[0, 0, 0, 0],
       [1, 0, 1, 0],
       [1, 0, 1, 0],
       [0, 0, 0, 0]
       ]

visit = [[0]*4 for _ in range(4)]
flag = 0 # 도착시 1로 바꿀 예정
def dfs(y, x):
    global flag
    if y == 3 and x == 3:
        flag = 1
        return
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        if visit[dy][dx] == 1:
            continue
        if arr[dy][dx] == 1:
            continue
        visit[dy][dx] = 1
        dfs(dy, dx)
        visit[dy][dx] = 0

visit[0][0] = 1
dfs(0, 0)       # y, x 좌표값

if flag == 1:
    print('갈 수 있어')
else:
    print('갈 수 없어')

print(visit)