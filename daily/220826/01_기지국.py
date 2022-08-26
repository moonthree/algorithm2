# 1
# 9
# XXXXXXXXX
# XXXHXXXXX
# XXHAHXXHX
# XXHHXXXXX
# XXXXXXXXX
# XXAHHXXXX
# XXHXXHAHX
# XXAHXXHXX
# XXHXHXXXX

def wifi(y, x, length):
    while length != 0:
        directy = [length, -length, 0, 0]
        directx = [0, 0, length, -length]
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if arr[dy][dx] == 'H':
                arr[dy][dx] = 'Z'
        length -= 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                wifi(i, j, 1)
            elif arr[i][j] == 'B':
                wifi(i, j, 2)
            elif arr[i][j] == 'C':
                wifi(i, j, 3)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1
    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end=' ')
    #     print()
    print(f'#{tc} {cnt}')