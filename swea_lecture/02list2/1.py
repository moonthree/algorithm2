# 00 01 02
# 10 11 12
# 20 21 22

# 00 01 02 12 22 2 1 20
#
test_case = int(input())

for t in range(test_case):
    N = int(input())

    directy = [0, 1, 0, -1]
    directx = [1, 0, -1, 0]

    arr = [[0]*N for i in range(N)]

    dy = 0
    dx = 0
    idx = 0
    num = 1

    while True:
        arr[dy][dx] = num
        num += 1

        y = dy + directy[idx]
        x = dx + directx[idx]

        if y < 0 or y > N-1 or x < 0 or x > N-1 or arr[y][x] != 0:
            idx += 1

        if idx == 4:
            idx = 0
        dy += directy[idx]
        dx += directx[idx]

        if num > N*N:
            break

    print(f'#{t+1}')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()