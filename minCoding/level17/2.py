arr = [5, 9, 4, 6, 1, 5, 8, 9]

idx, target = map(int, input().split())

offset = 0
for i in range(idx, len(arr)-1):
    if arr[i] == target:
        print(offset)
        break
    else:
        offset += 1