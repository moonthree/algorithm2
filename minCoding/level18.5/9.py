words = input()

bucket = [0]*ord('G')

for i in words:
    bucket[ord(i)] += 1

for i in range(len(bucket)):
    if bucket[i]:
        print(chr(i),end='')