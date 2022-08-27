dx, dy = map(int, input().split())
n = int(input())
arr = [[0]*dx for _ in range(dy)]
if n > dy*dx:
    print(0)
    exit()
for y in range(dy-1, -1, -1):
    for x in range(dx):
        arr[y][x] = [x+1, dy-y]

# for y in range(dy):
#     for x in range(dx):
#         print(arr[y][x], end=' ')
#     print()

seat = [[0]*dx for _ in range(dy)]

cnt = 1
directy = [-1, 0, 1, 0]
directx = [0, 1, 0, -1]
ddy = dy
ddx = 0
i = 0
while cnt != dy*dx+1:
    while True:
        if i > 3:
            i = 0
        ddy += directy[i]
        ddx += directx[i]
        if ddy < 0 or ddx < 0 or ddy > dy-1 or ddx > dx-1 or seat[ddy][ddx] != 0:
            ddy -= directy[i]
            ddx -= directx[i]
            i += 1
            break
        seat[ddy][ddx] = cnt
        cnt += 1

# for y in range(dy):
#     for x in range(dx):
#         print(seat[y][x], end=' ')
#     print()
flag = 0
for y in range(dy):
    for x in range(dx):
        if seat[y][x] == n:
            print(f'{arr[y][x][0]} {arr[y][x][1]}')
            flag = 1
            break
    if flag:
        break