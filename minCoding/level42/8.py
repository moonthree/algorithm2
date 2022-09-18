import copy

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
flag = 0
def dfs(level, y, x):
    global arr, flag
    if y == n - 1 and x == n - 1:
        flag = 1
        return
    if level > n*n:
        return
    miro(level, y, x)

def miro(level, a, b):
    global arr
    while a + b != 2*n-2:
        cnt = 0
        for i in range(4):
            dy = a + directy[i]
            dx = b + directx[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1 or arr[dy][dx] == 1:
                cnt += 1
                continue
            arr[dy][dx] = 1
            dfs(level+1, dy, dx)
        if cnt == 4:
            break
dfs(0, 0, 0)

if flag:
    print('가능')
else:
    print('불가능')