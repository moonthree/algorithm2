# 상하좌우 중 3곳 이상 물이면 잠기는 함수
# 큰 바다를 만들어서 X(섬)은 무조건 .(바다)안쪽에 있도록 넣어놨기 떄문에 편함
def GW(yy, xx):
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    cnt = 0
    for i in range(4):
        dy = directy[i] + yy
        dx = directx[i] + xx

        if arr_big[dy][dx] == '.':
            cnt += 1

    # 큰 바다에서 섬이 무조건 바다로 둘러싸여 있도록 만드느라
    # if arr[y][x] == 'X':
    #      arr_big[y + 1][x + 1] = 'X' 를 사용했으니

    # arr[yy - 1][xx - 1] = '.' 을 해주면 원래 바다의 'X' 위치를 찾을 수 있음
    if cnt > 2:
        arr[yy - 1][xx - 1] = '.'

# 입력 받기
y, x = map(int, input().split())
arr = [list(input()) for _ in range(y)]

# 기존 바다맵을 전부 .으로 감쌀 수 있는 큰 바다를 만듬
arr_big = [['.'] * (x + 2) for _ in range(y + 2)]

# 큰 바다에 섬 넣기
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == 'X':
            arr_big[y + 1][x + 1] = 'X'
            
#큰 바다 출력 테스트
# for y in range(len(arr_big)):
#     for x in range(len(arr_big[y])):
#         print(arr_big[y][x], end='')
#     print()

# 큰 바다에서 'X'를 찾으면 GW 함수로 X의 좌표값 가지고 이동
for y in range(len(arr_big)):
    for x in range(len(arr_big[y])):
        if arr_big[y][x] == 'X':
            GW(y, x)

# 섬의 최대, 최소 좌표값 찾기
max_y = 0
max_x = 0
min_x = int(21e8)
min_y = int(21e8)
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == 'X':
            if max_y < y:
                max_y = y
            if min_y > y:
                min_y = y
            if max_x < x:
                max_x = x
            if min_x > x:
                min_x = x
print(min_x)
print(min_y)
for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        print(arr[y][x], end='')
    print()

# for y in range(len(arr)):
#     for x in range(len(arr[y])):
#         print(arr[y][x], end='')
#     print()