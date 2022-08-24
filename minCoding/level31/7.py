n = int(input())

arr = [input() for _ in range(n)]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

for i in range(len(arr)-1):
    if len(arr[i]) == len(arr[i+1]):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

for i in range(len(arr)-1):
    if len(arr[i]) == len(arr[i+1]):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]





for i in arr:
    print(i)
