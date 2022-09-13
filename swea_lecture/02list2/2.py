# 00 01 02
# 10 11 12
# 20 21 22

for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    directy = [-1, 0, 1, 0]
    directx = [0, 1, 0, -1]

    def sum_cross(y, x):
        sums = 0
        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]
            if dy < 0 or dy > N-1 or dx < 0 or dx > N-1:
                continue
            sums += abs(arr[dy][dx] - arr[y][x])
        return sums

    sum_arr = 0
    for i in range(N):
        for j in range(N):
            sum_arr += sum_cross(i, j)

    print(f'#{t} {sum_arr}')