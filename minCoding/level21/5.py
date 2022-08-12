arr = [list(input()) for _ in range(3)]

n = len(arr)

long = len(arr[0])
long_idx = 0
for i in range(n):
    if len(arr[i]) > long:
        long = len(arr[i])
        long_idx = i

arr[0], arr[long_idx] = arr[long_idx], arr[0]

for i in range(n):
    for j in range(len(arr[i])):
        print(arr[i][j], end='')
    print()

