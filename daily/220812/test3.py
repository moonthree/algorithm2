arr = [[4, 7, 1, 8], [3, 5, 9, 2], [5, 9, 5, 9], [1, 2, 9, 7]]

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

sum_up = 0
sum_down = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i+j < 3:
            sum_up += arr[i][j]
        elif i+j > 3:
            sum_down += arr[i][j]

print(sum_up, sum_down)