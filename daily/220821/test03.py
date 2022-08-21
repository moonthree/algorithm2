# direct
# 위 아래 좌 우 보았을 때 기준 좌표보다 크면 그 기준 좌표를 산 봉우리라고 한다.
'''
4 5
2 4 2 1 5
1 2 1 4 3
2 2 2 4 2
1 7 3 2 3
'''

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def mountain(y, x):
    direct_y = [-1, 0, 1, 0]
    direct_x = [0, 1, 0, -1]

    for i in range(4):
        dy = direct_y[i] + y
        dx = direct_x[i] + x

        if dy < 0 or dx < 0 or dy > n-1 or dx > m-1:
            continue
        if arr[y][x] <= arr[dy][dx]:
            return 0
    return 1

cnt = 0
for y in range(n):
    for x in range(m):
        cnt += mountain(y, x)

print(cnt)