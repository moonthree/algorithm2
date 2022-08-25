n = int(input())

arr = [input() for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

for i in range(n-1, 0, -1):
    if len(arr[i]) == len(arr[i-1]):
        for j in range(len(arr[i])):
            if arr[i][j] > arr[i-1][j]:
                break
            elif arr[i][j] < arr[i-1][j]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                break

for i in arr:
    print(i)