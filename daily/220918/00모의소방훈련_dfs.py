n = int(input())

arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]
y, x = map(int, input().split())

# 1. 소화기 위치 찾기
# 2. 소화기 위치 방향으로 이동
# 3. 불 위치 찾기
# 4. 불 방향으로 이동

direct_y = [0, 0, -1, 1]
direct_x = [1, -1, 0, 0]
flag = 0
MIN = 21e8
MIN2 = 21e8
water_y = 0
water_x = 0
def dfs(level, yy, xx, move):
    global MIN, flag, water_x, water_y

    if arr[yy][xx] == 'A':
        if move < MIN:
            MIN = move
            water_y = yy
            water_x = xx
        return

    visited[yy][xx] = 1
    miro(level, yy, xx, move)
    visited[yy][xx] = 0

def miro(level, yy, xx, move):
    global visited
    direct_y = [0, 0, -1, 1]
    direct_x = [1, -1, 0, 0]
    for i in range(4):
        dy = direct_y[i] + yy
        dx = direct_x[i] + xx

        if dy < 0 or dx < 0 or dy > n-1 or dx > n-1 or arr[dy][dx] == '#' or arr[dy][dx] == '$' or visited[dy][dx] == 1:
            continue
        dfs(level+1, dy, dx, move+1)

visited[y][x] = 1
dfs(0, y, x, 0)


def fire(level, fy, fx):
    global MIN2, visited2
    if arr[fy][fx] == '$':
        MIN2 = min(level, MIN2)
        return
    direct_y = [1, 0, -1, 0]
    direct_x = [0, -1, 0, -1]
    for i in range(4):
        dy = direct_y[i] + fy
        dx = direct_x[i] + fx

        if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1 or arr[dy][dx] == '#' or visited2[dy][
            dx] == 1:
            continue
        visited2[dy][dx] = 1
        fire(level + 1, dy, dx)
        visited2[dy][dx] = 0

visited2[water_y][water_x] = 1
fire(0, water_y, water_x)
print(MIN2+MIN)