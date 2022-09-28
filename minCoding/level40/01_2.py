arr = [list(map(int, input().split())) for _ in range(4)]

arr1 = [[0] * 4 for _ in range(4)]

for i in range(1, 4):
    arr1[0][i] = arr1[0][i - 1] + arr[0][i]
    arr1[i][0] = arr1[i - 1][0] + arr[i][0]

for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        arr1[i][j] = min(arr1[i - 1][j], arr1[i][j - 1]) + arr[i][j]

# for i in range(4):
#     for j in range(4):
#         print(arr1[i][j], end=' ')
#     print()

x, y = 3, 3
directy = [-1, 0]
directx = [0, -1]
used = [[0] * 4 for _ in range(4)]
used[3][3] = 1
arr3 = []
while x != 0 or y != 0:
    arr3.append([y,x])
    ty, tx = 0, 0
    MIN = 21e8
    for i in range(2):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3 or used[dy][dx] == 1:
            continue
        if MIN >= arr1[dy][dx]:
            MIN = arr1[dy][dx]
            ty, tx = dy, dx
    y, x = ty, tx

print('0,0')
while arr3:
    a = arr3.pop()
    print(f'{a[0]},{a[1]}')