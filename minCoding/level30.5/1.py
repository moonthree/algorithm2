k = int(input())

arr = [12, 3, 6, 9]

n = k//90
for i in range(n):
    arr[0], arr[1] = arr[1], arr[0]
    arr[0], arr[2] = arr[2], arr[0]
    arr[0], arr[-1] = arr[-1], arr[0]


print(arr[0], end=' ')
print(arr[3], end=' ')
print(arr[1], end=' ')
print(arr[2])