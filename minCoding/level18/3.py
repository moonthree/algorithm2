arr = [[1, 3, 3, 5, 1], [3, 6, 2, 4, 2], [1, 9, 2, 6, 5]]

n = int(input())

bucket = [0]*10

for i in range(len(arr)):
    for j in range(len(arr[i])):
        bucket[arr[i][j]] += 1

for i in range(len(bucket)):
    if bucket[i] == n:
        print(i, end=' ')
