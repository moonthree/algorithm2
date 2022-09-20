# n = 지도 세로 크기
# m = 지도 가로 크기
# dice_x = 주사위 x좌표
# dice_y = 주사위 y좌표
# k = 명령 횟수

n, m, dice_y, dice_x, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move_order = list(map(int, input().split()))

# 0 = 아래, 1 = 서쪽, 2 = 북쪽, 3 = 동쪽, 4 = 남쪽, 5 = 위
dice = [0] * 6

# 이동 방향
# 4 = 남쪽, 3 = 북쪽, 2 = 서쪽, 1 = 동쪽
directy = [0, 0, 0, -1, 1]
directx = [0, 1, -1, 0, 0]

# 위가 북쪽으로, 아래가 남쪽으로, 북쪽이 아래로, 남쪽이 위로
def dice_move(yy, xx, ii):
    global dice_y
    global dice_x
    dy = directy[ii] + yy
    dx = directx[ii] + xx
    if dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1:
        return
    dice_y += directy[ii]
    dice_x += directx[ii]
    if ii == 4:
        dice[5], dice[0], dice[2], dice[4] = dice[4], dice[2], dice[5], dice[0]
    elif ii == 3:
        dice[5], dice[0], dice[2], dice[4] = dice[2], dice[4], dice[0], dice[5]
    elif ii == 2:
        dice[5], dice[3], dice[0], dice[1] = dice[1], dice[5], dice[3], dice[0]
    elif ii == 1:
        dice[5], dice[3], dice[0], dice[1] = dice[3], dice[0], dice[1], dice[5]
    if arr[dy][dx] == 0:
        arr[dy][dx] = dice[0]
    else:
        dice[0] = arr[dy][dx]
        arr[dy][dx] = 0
    print(dice[5])


for i in move_order:
    dice_move(dice_y, dice_x, i)



# 주사위 굴리기 시작
# 첫 start = 0이 밑면, 5가 윗면, 3이 오른쪽(동쪽), 2가 북쪽
# 4 남쪽으로 구르면 -> 주사위 4가 아래로
# 아래(남쪽)으로 구르면 뭐지
# 동쪽은 동쪽, 서쪽은 서쪽,
# 위가 남쪽으로, 아래가 북쪽으로, 북쪽이 위로, 남쪽이 아래로

# 위쪽(북쪽)으로 구르면 뭐지
# 동쪽은 동쪽, 서쪽은 서쪽,
# 위가 북쪽으로, 아래가 남쪽으로, 북쪽이 아래로, 남쪽이 위로

# 동쪽(오른쪽)으로 구르면 뭐지
# 북쪽은 북쪽, 남쪽은 남쪽,
# 위가 동쪽으로, 동쪽이 아래로, 아래가 서쪽으로, 서쪽이 위로

# 서쪽(왼쪽)으로 구르면 뭐지
# 북쪽은 북쪽, 남쪽은 남쪽,
# 위가 서쪽으로, 동쪽이 위로, 아래가 동쪽으로, 서쪽이 아래로
# okay~~~~
# 주사위 굴리기 끝

# 시작점에서 주사위를 굴리면..
# 구르고, 위치의 숫자를 아랫면에 찍고, 윗면의 숫자를 출력한다.
# 만약 맵을 벗어난 명령은 무시한다.
# 0 = 아래, 1 = 서쪽, 2 = 북쪽, 3 = 동쪽, 4 = 남쪽, 5 = 위

