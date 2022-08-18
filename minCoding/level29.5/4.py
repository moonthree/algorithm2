arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []

for i in range(4):
    if arr[i] > arr2[i]:
        result.append(arr2[i])
        result.append(arr[i])
    else:
        result.append(arr[i])
        result.append(arr2[i])

for i in result:
    print(i, end=' ')