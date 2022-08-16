arr = [[0]*4 for _ in range(4)]
arr2 = [list(map(int, input().split())) for _ in range(3)]

# 00 01 02
# 10 11 12
# 11 12 22

for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        arr[i][j] = arr2[i][j]
        arr[i][3] += arr2[i][j]
        arr[3][j] += arr2[i][j]
        if i == j:
            arr[3][3] += arr2[i][j]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()