from collections import deque
def move(y, x):
    global shark_level, cnt, arr
    distance = [[0]*n for _ in range(n)]
    q = deque()
    q.append((y, x, 1))
    distance[y][x] = 1

    while q:
        nowy, nowx, level = q.popleft()
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx

            if dy < 0 or dx < 0 or dy > n-1 or dx >n-1:
                continue
            if arr[dy][dx] > shark_level or distance[dy][dx] != 0:
                continue
            distance[dy][dx] = level
            q.append((dy, dx, level+1))
    temp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                if arr[i][j] < shark_level:
                    temp.append([distance[i][j], i, j])
    if temp:
        temp.sort(key=lambda x: (-x[0], -x[1], -x[2]))
        shark_level += 1
        cnt += temp[0][0]
        arr[temp[0][1]][temp[0][2]] = 0
        move(temp[0][1], temp[0][2])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

shark_level = 2
cnt = 0


for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            move(i, j)




print(cnt)

