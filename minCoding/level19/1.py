arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]

y, x = map(int, input().split())

directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

sums = 0

for i in range(4):
    dy = directy[i] + y  # 기준점으로부터 y에 입력받은 값을 더한 값
    dx = directx[i] + x  # 기준점으로부터 x에 입력받은 값을 더한 값

    if dy<0 or dy>2 or dx<0 or dx>2:
        continue

    sums += arr[dy][dx]
    debug = 1

print(sums)