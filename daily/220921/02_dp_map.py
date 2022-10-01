arr = [
    [0, 1, 1, 9],
    [4, 2, 2, 3],
    [1, 3, 4, 1],
    [3, 7, 8, 0]
]

arr1 = [[0] * 4 for _ in range(4)]

for i in range(1, 4):
    arr1[0][i] = arr1[0][i - 1] + arr[0][i]
    arr1[i][0] = arr1[i - 1][0] + arr[i][0]

for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        arr1[i][j] = min(arr1[i - 1][j], arr1[i][j - 1]) + arr[i][j]


print(arr1[3][3])
