n = int(input())

arr = [list(map(str, input().split())) for _ in range(n)]
arr.sort()
for i in arr:
    print(i[0], end=' ')
    print(i[1])