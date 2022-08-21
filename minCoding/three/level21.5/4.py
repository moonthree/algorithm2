arr = [list(input()) for _ in range(4)]

arr2 = [['_']*3 for _ in range(4)]

for y in range(len(arr)-1, -1, -1):
    for x in range(len(arr[y])-1, -1, -1):
        if arr[y][x] != '_':
            i = 0
            while arr2[len(arr)-1-i][x] != '_':
                i += 1
            arr2[len(arr)-1-i][x] = arr[y][x]

for y in range(len(arr2)):
    for x in range(len(arr2[y])):
        print(arr2[y][x], end='')
    print()


