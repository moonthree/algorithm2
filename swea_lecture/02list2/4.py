test_case = int(input())

for t in range(test_case):
    N = int(input())
    color_list = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0]*10 for _ in range(10)]

    for i in range(len(color_list)):
        for y in range(color_list[i][0], color_list[i][2]+1):
            for x in range(color_list[i][1], color_list[i][3]+1):
                if color_list[i][-1] == 1:
                    arr[y][x] += 1
                elif color_list[i][-1] == 2:
                    arr[y][x] += 100

    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 101:
                cnt += 1

    print(f'#{t+1} {cnt}')
