arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    a, b, c, d = map(int, input().split())

    for y in range(b, d):
        for x in range(a, c):
            arr[y][x] = 1


cnt = 0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == 1:
            cnt += 1

print(cnt)