arr = [[1, 5, 3], [4, 5, 5], [3, 3, 5], [4, 6, 2]]
a, b = map(int, input().split())

for y in range(len(arr)):
    for x in range(len(arr[y])):
        if a <= arr[y][x] <= b:
            arr[y][x] = 0

for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == 0:
            print('#', end=' ')
        else:
            print(arr[y][x], end=' ')
    print()