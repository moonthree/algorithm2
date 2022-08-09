arr = [[3, 5, 9], [4, 2, 1], [1, 1, 5]]

input_arr = [list(map(int, input().split())) for _ in range(3)]

arr_sum = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if input_arr[i][j] == 1:
            arr_sum += arr[i][j]
print(arr_sum)
