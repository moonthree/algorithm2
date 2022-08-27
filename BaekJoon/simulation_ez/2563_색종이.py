arr = [[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    for y in range(a, a+10):
        for x in range(b-10, b):
            arr[y][x] = 1

cnt = 0
for y in range(len(arr)):
    for x in range(len(arr)):
        if arr[y][x] == 1:
            cnt += 1

print(cnt)

