arr = list(map(int, input().split()))

pivot = arr[0]

while True:
    a = 0
    a_idx = 0
    b = 0
    b_idx = 0

    for i in range(1, len(arr)):
        if arr[i] > pivot:
            a = arr[i]
            a_idx = i
            break
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < pivot:
            b = arr[i]
            b_idx = i
            break
    if a_idx > b_idx:
        arr[0], arr[b_idx] = arr[b_idx], arr[0]
        break

    arr[a_idx], arr[b_idx] = arr[b_idx], arr[a_idx]


for i in arr:
    print(i, end=' ')