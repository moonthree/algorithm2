arr = [[65000, 35, 42, 70], [70, 35, 65000, 1300], [65000, 30000, 38, 42]]

bucket = [0]*650001

for i in range(len(arr)):
    for j in range(len(arr[i])):
        bucket[arr[i][j]] += 1

max_idx = 0
for i in range(len(bucket)):
    if bucket[max_idx] < bucket[i]:
        max_idx = i

print(max_idx)