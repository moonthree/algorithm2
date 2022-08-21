# 선택정렬

arr = [4, 7, 8, 9, 1]

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)