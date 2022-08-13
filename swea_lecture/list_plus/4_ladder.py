# 아래, 오른쪽, 왼쪽으로만 이동
# 아래로만 이동하다가 오른쪽 혹은 왼쪽에 1이 있으면 그 방향으로 이동 후 다시 아래로 이동

# 10개의 테스트케이스, 100*100의 이차원 배열
# 5*5에서 테스트 ㄱ
import sys
sys.stdin = open("4_input.txt", "r")

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 아래, 오른쪽, 왼쪽
    directy = [1, 0, 0]
    directx = [0, 1, -1]

    def ladder(start):
        y = 0
        x = start
        a = 0
        b = start
        # 1을 따라가고 이미 간 장소는 3으로 만들어서 다시 못돌아오게 함
        while y != 98:
            dircetion = 0
            for i in range(3):
                dy = directy[i] + y
                dx = directx[i] + x
                if dx < 0 or dy < 0 or dx > 99 or dy > 99:
                    continue
                if arr[dy][dx] == 1:
                    dircetion = i

            ndy = directy[dircetion] + y
            ndx = directx[dircetion] + x
            y += directy[dircetion]
            x += directx[dircetion]

            arr[ndy][ndx] = 3

        # 다음 사다리에서 중복된 장소를 갈 수도 있으므로 3을 다시 1로 초기화함
        while a != 98:
            dircetion = 0
            for i in range(3):
                dy = directy[i] + a
                dx = directx[i] + b
                if dx < 0 or dy < 0 or dx > 99 or dy > 99:
                    continue
                if arr[dy][dx] == 3:
                    dircetion = i

            ndy = directy[dircetion] + a
            ndx = directx[dircetion] + b
            a += directy[dircetion]
            b += directx[dircetion]

            arr[ndy][ndx] = 1

        if arr[y+1][x] == 2:
            return 1
        else:
            return 0

    win = 0

    for i in range(len(arr[0])):
        if arr[0][i] == 1:
            if ladder(i):
                win = i
                break

    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         print(arr[i][j], end=' ')
    #     print()

    print(f'#{tc} {win}')

