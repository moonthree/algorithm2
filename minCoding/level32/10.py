n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]
bit = [list(map(int, input().split())) for _ in range(n)]

arr = []

for y in range(n):
    for x in range(n):
        if bit[y][x] == 1:
            arr.append(num[y][x])

sort1 = sorted(arr, key=lambda x: (-arr.count(x), x))
print(*sort1)



