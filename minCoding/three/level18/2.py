arr = [list(map(int, input().split())) for _ in range(3)]

bucket = [0]*10

for i in range(len(arr)):
    for j in range(len(arr[i])):
        bucket[arr[i][j]] += 1

for i in range(1, len(bucket)):
    if bucket[i] == 0:
        print(i, end=' ')