vect = [[3, 7, 3], [2, 2, 4], [2, 2, 5]]

target = list(map(int, input().split()))

bucket = [0]*len(target)

for i in range(len(target)):
    for j in range(len(vect)):
        for k in range(len(vect[j])):
            if target[i] == vect[j][k]:
                bucket[i] += 1

max_idx = 0
max_num = bucket[0]
for i in range(len(bucket)):
    if bucket[i] > max_num:
        max_num = bucket[i]
        max_idx = i

print(target[max_idx])