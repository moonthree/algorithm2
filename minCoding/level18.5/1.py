arr = [['G', 'K', 'G'], input().split()]

bucket = [0]*ord('a')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        bucket[ord(arr[i][j])] += 1

flag = 0

for i in range(len(bucket)):
    if bucket[i] >= 3:
        flag += 1
        break

if flag:
    print('있음')
else:
    print('없음')