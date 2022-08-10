arr = [input() for _ in range(3)]

bucket = [0]*(ord('z')+1)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        bucket[ord(arr[i][j])] += 1


flag = 0
for i in bucket:
    if i > 1:
        flag += 1

if flag:
    print('No')
else:
    print('Perfect')