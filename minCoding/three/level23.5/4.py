arr = [[3, 5, 4, 1],
       [1, 1, 2, 3],
       [6, 7, 1, 2]]
arr_new = [[3, 5, 4, 1],
           [1, 1, 2, 3],
           [6, 7, 1, 2]]
arr2 = list(map(int, input().split()))

for k in range(len(arr2)):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr2[k]:
                if k == 3:
                    arr_new[i][j] = arr2[0]
                else:
                    arr_new[i][j] = arr2[k + 1]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr_new[i][j], end=' ')
    print()
