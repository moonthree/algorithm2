arr = [[0 for _ in range(4)] for _ in range(7)]

for i in range(7):
    for j in range(4):
        arr[i][j] = j+1 + i*4

nums = list(map(int, input().split()))

for i in nums:
    for j in range(4):
        arr[i][j] = 0

for i in arr:
    for j in range(4):
        print(i[j], end=' ')
    print()