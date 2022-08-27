n = int(input())
arr = list(map(int, input().split()))
arr2 = []
for i in range(n):
    arr2.insert(i-arr[i], i+1)


for i in arr2:
    print(i)

