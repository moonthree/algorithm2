n = int(input())

arr = []
for _ in range(n):
    y, x, c = map(int, input().split())
    a = list(str(c))
    arr.append(a)
print(arr)
num = int(input())
wind = list(map(int, input().split()))

for i in range(num):
    for j in range(n):
        if arr[j]:
            top = int(arr[j].pop())
            if top > wind[i]:
                arr[j].append(str(top - wind[i]))
print(arr)
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]:
            cnt += 1

print(cnt)





