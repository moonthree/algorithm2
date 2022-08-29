import sys
sys.stdin = open("7_input.txt", "r")

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    directx = [0, -1, 1]
    directy = [-1, 0, 0]

    start_x = 0
    start_y = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                start_x = j
                start_y = i

    while start_y != 0:
        for i in range(3):
            ny = start_y + directy[i]
            nx = start_x + directx[i]
            if ny < 0 or nx < 0 or ny > 99 or nx > 99: continue

            if arr[start_y][start_x-1] ==1:
                i = 1
            elif arr[start_y][start_x+1] == 1:
                i = 2
            elif arr[start_y-1][start_x] == 1:
                i = 0

            if arr[ny][nx] == 1:
                arr[start_y][start_x] = 3
                start_x += directx[i]
                start_y += directy[i]

    print(f'#{tc} {start_x}')

    # for n in range(100):
    #     for m in range(100):
    #         print(arr[n][m], end =' ')
    #     print()