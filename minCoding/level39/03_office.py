n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr2 = sorted(arr, key=lambda x: x[1])
cnt = 0
for i in range(n-1):
    if arr[i][1] <= arr[i+1][0]:
        cnt += 1

print(cnt)