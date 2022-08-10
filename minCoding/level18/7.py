arr = [['A', 'B', 'C'], ['A', 'G', 'H'], ['H', 'I', 'J'], ['K', 'A', 'B'], ['A', 'B', 'C']]

bucket = [0]*ord('a')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        bucket[ord(arr[i][j])] += 1

for i in range(len(bucket)):
    if bucket[i] != 0:
        for _ in range(bucket[i]):
            print(chr(i), end='')