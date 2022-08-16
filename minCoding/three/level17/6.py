arr1 = [[0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
arr2 = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        if arr1[i][j]+arr2[i][j] == 0:
            print(f'({i},{j})')