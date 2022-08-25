n = int(input())
arr = list(map(int, input().split()))
for i in range(n-2):
    if arr[i] == arr[i+1] == arr[i+2]:
        for j in range(i, i+3):
            arr.pop(j)
            arr.insert(j, 0)

arr.sort()

for i in arr:
    if i != 0:
        print(i, end=' ')
