arr = [list(map(int, input().split())) for _ in range(5)]

# 00 01 02
# 10 11 12
# 20 21 22

directy = [-1, -1, -1, 0, 1, 1, 1, 0]
directx = [-1, 0, 1, 1, 1, 0, -1, -1]

def stableCell(y, x):
    cnt = 0
    for i in range(len(directy)):
        dy = directy[i] + y
        dx = directx[i] + x

        if dy < 0 or dy > 4 or dx < 0 or dx > 3:
            continue
        if arr[dy][dx] != 0:
            cnt += 1
            break
    return cnt

unstable = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            unstable += stableCell(i, j)
        
if unstable:
    print('불안정한 상태')
else:
    print('안정된 상태')