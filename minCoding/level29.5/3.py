arr = [list(map(int, input().split())) for _ in range(3)]

for y in range(len(arr)):
    cnt = 0
    a = arr[y][0]
    for x in range(1, len(arr[y])):
        if a == arr[y][x]:
            cnt += 1
    if cnt == 2:
        print(a)
    else:
        print('x')

