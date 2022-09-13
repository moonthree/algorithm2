# 1. 농장의 크기는 항상 홀수
# 2. 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태

# 00 01 02
# 10 11 12
# 20 21 22
# 크기 : 3
# 사이드 : 1

# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44
# 크기 : 5
# 사이드 : 00~ 02

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    profit = 0
    for i in range(n):
        for j in range(n):
            profit += int(arr[i][j])
    if n > 1:
        # 상단
        for i in range(n // 2 + 1):
            # 왼쪽
            for j in range(0, n // 2 - i):
                profit -= int(arr[i][j])
            # 오른쪽
            for j in range(n // 2 + 1 + i, n):
                profit -= int(arr[i][j])
        # 하단
        temp = 1
        for i in range(n // 2 + 1, n):
            # 왼쪽
            for j in range(temp):
                profit -= int(arr[i][j])

            # 오른쪽
            for j in range(n-1, n-1-temp, -1):
                profit -= int(arr[i][j])
            #     print(arr[i][j], end='')
            # print()
            temp += 1
    print(f'#{tc} {profit}')
