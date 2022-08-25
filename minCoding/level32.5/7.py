arr = [list(map(int, input().split())) for _ in range(4)]

ground = []

def rect(y, x):
    dy = y
    dx = x
    while arr[dy][x] != 0 and dy < 3:
        dy += 1

    flag = 0
    for j in range(x, 8):
        for i in range(y, dy):
            if arr[i][j] == 0:
                flag += 1
                break
        if flag:
            break
        dx += 1
    ssum = 0
    for i in range(y, dy):
        for j in range(x, dx):
            ssum += arr[i][j]
    ground.append(ssum)

for i in range(4):
    for j in range(8):
        if arr[i][j] != 0:
            rect(i, j)

print(max(ground))




