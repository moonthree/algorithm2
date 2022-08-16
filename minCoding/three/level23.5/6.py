arr_input = [list(input()) for _ in range(4)]

arr = [['A', 'B', 'C', 'D'],
       ['B', 'B', 'A', 'B'],
       ['C', 'B', 'A', 'C'],
       ['B', 'A', 'A', 'A'],
       ]

bucket = [0]*(ord('Z')+1)

for i in range(len(arr_input)):
    for j in range(len(arr_input[i])):
        if arr_input[i][j] == arr[i][j]:
            bucket[ord(arr[i][j])] += 1

maximum = int(-21e8)
idx = 0
for i in range(len(bucket)):
    if bucket[i] > maximum:
        maximum = bucket[i]
        idx = i

print(chr(idx))