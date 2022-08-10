arr = [[2, 7, 3], [8, 5, 9], [7, 4, 6]]

a, b = map(int, input().split())
sums = 0

arr_point = []

for y in range(len(arr)):
    for x in range(len(arr[y])):
        arr_point.append([y, x])

for i in arr_point:
    if [a+1, b] == i:
        sums += arr[a+1][b]
    elif [a-1, b] == i:
        sums += arr[a-1][b]
    elif [a, b+1] == i:
        sums += arr[a][b+1]
    elif [a, b-1] == i:
        sums += arr[a][b-1]

print(sums)