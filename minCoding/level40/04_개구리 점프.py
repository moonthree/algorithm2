arr = [list(map(int, input().split())) for _ in range(7)]


arr2 = [[0]*3 for _ in range(7)]
arr2[0][0] = 1

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        if arr[i][j] == 0:
            continue
        if j == 0:
            arr2[i][j] = max(arr2[i - 1][j], arr2[i - 1][j + 1]) + arr[i][j]
        elif j == 1:
            arr2[i][j] = max(arr2[i - 1][j - 1], arr2[i - 1][j], arr2[i - 1][j + 1]) + arr[i][j]
        elif j == 2:
            arr2[i][j] = max(arr2[i - 1][j - 1], arr2[i - 1][j]) + arr[i][j]


print(max(arr2[6]))
