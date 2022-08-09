arr = [[3, 1, 9], [7, 2, 1], [1, 0, 8]]

mask = [list(map(int, input().split())) for _ in range(3)]

cnt = 0
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 1:
            if 3 <= arr[i][j] <= 5:
                cnt += 1

if cnt == 0:
    print('미발견')
else:
    print('발견')