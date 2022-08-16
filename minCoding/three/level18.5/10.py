words = input()

bucket = [0]*(ord('z')+1)

for i in words:
    bucket[ord(i)] += 1

for i in range(len(bucket)):
    if bucket[i] != 0:
        print(f'{chr(i)}:{bucket[i]}')