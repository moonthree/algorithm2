array = [[0]*4 for _ in range(4)]

for _ in range(2):
    arr = [list(map(int, input().split())) for _ in range(4)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                array[i][j] += 1

cnt = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == 2:
            cnt += 1

if cnt:
    print('걸리다')
else:
    print('걸리지않는다')