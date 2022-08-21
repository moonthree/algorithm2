arr = [[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 0, 0],
       [0, 1, 2, 0, 2, 1, 0],
       [0, 0, 1, 2, 1, 0, 0],
       [0, 0, 2, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]
       ]

a, b = map(int, input().split())

# 00 01 02
# 10 11 12
# 20 21 22

directy = [-1, 0, 1, 0]
directx = [0, 1, 0, -1]

def catch(y, x):
    arr[y][x] = 1
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                white = 0
                for k in range(4):
                    dy = directy[k] + i
                    dx = directx[k] + j
                    if dy < 0 or dx < 0 or dy > 6 or dx > 6:
                        continue
                    if arr[dy][dx] == 1:
                        white += 1
                if white == 4:
                    cnt += 1
    return cnt

print(catch(a, b))
