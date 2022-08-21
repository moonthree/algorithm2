arr = [3, 5, 1, 9, 7]

direct = [input() for _ in range(4)]
# 5 3 1 9 7
# 1 3 5 9 7
# 9 3 5 1 7
# 7 3 5 1 9

# 3 5 1 7 9
# 3 5 9 7 1
for i in range(len(direct)):
    if direct[i] == 'R':
        for j in range(1, len(arr)):
            arr[0], arr[j] = arr[j], arr[0]
    elif direct[i] == 'L':
        for j in range(len(arr)-1, -1, -1):
            arr[len(arr)-1], arr[j] = arr[j], arr[len(arr)-1]

for i in arr:
    print(i, end=' ')
