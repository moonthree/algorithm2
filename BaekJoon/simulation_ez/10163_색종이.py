n = int(input())

arr = [[-1]*1001 for _ in range(1001)]

max_y = 0
max_x = 0
for i in range(n):
    a, b, c, d = map(int, input().split())

    if max_y < b+d+1:
        max_y = b+d+1
    if max_x < a+c+1:
        max_x = a+c+1

    for y in range(b, b+d):
        for x in range(a, a+c):
            arr[y][x] = i


for i in range(n):
    cnt = 0

    for y in range(max_y):
        for x in range(max_x):
            if arr[y][x] == i:
                cnt += 1
    print(cnt)