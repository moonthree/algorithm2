
import sys
sys.stdin = open("7_input.txt", "r")


# 밑에서 2를 찾고 올라가기
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 위, 오른쪽, 왼쪽
    directy = [-1, 0, 0]
    directx = [0, 1, -1]

    def ladder(start):
        y = 99
        x = start        # 1을 따라가고 이미 간 장소는 3으로 만들어서 다시 못돌아오게 함
        while y != 0:
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
        return x

    for i in range(len(arr[99])):
        if arr[99][i] == 2:
            print(f'#{tc} {ladder(i)}')
            break

