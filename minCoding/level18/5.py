words = input()

arr = []
for i in words:
    arr.append(i)

bucket = [0]*ord('a')

for i in range(len(arr)):
    bucket[ord(arr[i])] += 1

max_idx = 0
max_chr = 0
for i in range(len(bucket)):
    if bucket[i] > max_idx:
        max_idx = bucket[i]
        max_chr = i

print(chr(max_chr))