n, target = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
l = 0
r = 0
for i in range(n):
    if arr[i] + arr[i+1] == target:
        cnt += 1

print(cnt)