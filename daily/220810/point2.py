# 배열에서 본인 좌표 포함한 상하좌우의 합 중 최대값과 해당 좌표 구하기

arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]

directy = [-1, 1, 0, 0, 0]
directx = [0, 0, 0, -1, 1]

Max = int(-21e8)
Maxy = 0
Maxx = 0

def getSum(y, x):
    sum = 0
    for i in range(5):
        dy = directy[i]+y
        dx = directx[i]+x
        if dy < 0 or dy > 2 or dx < 0 or dx > 2:
            continue
        sum += arr[dy][dx]
    return sum

for i in range(3):
    for j in range(3):
        ret = getSum(i, j)
        if ret > Max:
            Max = ret
            Maxy = i
            Maxx = j

print(Maxy, Maxx)
print(Max)