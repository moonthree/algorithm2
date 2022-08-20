n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# 00 01 02
# 10 11 12
# 20 21 22

direct_y = [-1, 0, 1, 0]
direct_x = [0, 1, 0, -1]

def mountain(y, x):
    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]

        if dy < 0 or dx < 0 or dy > n-1 or dx > m-1:
            continue
        if arr[y][x] <= arr[dy][dx]:
            return 0
    return 1


cnt = 0
for y in range(n):
    for x in range(m):
        if mountain(y, x) == 1:
            cnt += 1

print(cnt)