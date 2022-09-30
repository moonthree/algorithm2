def move(k):
    global arr
    for i in arr:
        print(i)
    print('aaaaaaaaaaaaaaaaaaaaaaa처음')
    for i in range(len(arr)):
        arr[i][0] += dy[arr[i][3]]
        arr[i][1] += dx[arr[i][3]]
    for i in arr:
        print(i)
    print('aaaaaaaaaaaaaaaaaaaaaaa위치 바꾸기')
    mix(k)


def mix(k):
    global arr
    used = [0]*len(arr)
    arr2 = []
    for i in range(len(arr)):
        temp = []
        if used[i]:
            continue
        for j in range(len(arr)):
            if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1] and not used[j]:
                used[j] = 1
                temp.append([arr[j][0], arr[j][1], arr[j][2], arr[j][3]])
        temp2 = sorted(temp, key=lambda x:-x[2])
        #print(temp2)
        for j in range(1, len(temp2)):
            temp2[0][2] += temp2[j][2]
        arr2.append(temp2[0])
    arr = []
    for i in arr2:
        arr.append(i)
    for i in arr:
        print(i)
    print('aaaaaaaaaaaaaaaaaaaaaaa 합치기')
    red(k)


def red(k):
    global arr
    for i in range(len(arr)):
        if arr[i][0] == 0 or arr[i][1] == 0 or arr[i][0] == n or arr[i][1] == n:
            arr[i][2] = arr[i][2] // 2
            if arr[i][3] == 1 or arr[i][3] == 3:
                arr[i][3] = arr[i][3] + 1
            elif arr[i][3] == 2 or arr[i][3] == 4:
                arr[i][3] = arr[i][3] - 1
    for i in range(len(arr)):
        if arr[i][2] == 0:
            arr[i].pop()
    for i in arr:
        print(i)
    print('aaaaaaaaaaaaaaaaaaaaaaa red존')
    print()
    #quit()


t = int(input())
for tc in range(1, t + 1):
    # 셀의 수, 격리 시간, 미생물 군집의 개수
    n, m, k = map(int, input().split())

    # 세로:0, 가로:1, 미생물수:2, 이동방향:3
    arr = [list(map(int, input().split())) for _ in range(k)]

    # 이동방향 (상:1, 하:2, 좌:3, 우:4)
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]

    for _ in range(100):
        move(k)
    cnt = 0
    for i in range(len(arr)):
        #print(arr[i][2])
        cnt += arr[i][2]
    print(f'#{tc} {cnt}')

# 1
# 7 2 9
# 1 1 7 1
# 2 1 7 1
# 5 1 5 4
# 3 2 8 4
# 4 3 14 1
# 3 4 3 3
# 1 5 8 2
# 3 5 100 1
# 5 5 1 1

# 1
# 7 1 5
# 0 1 7 3
# 0 5 7 4
# 3 0 7 1
# 5 0 7 2
# 0 5 7 3
