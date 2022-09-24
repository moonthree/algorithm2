n = int(input())
arr = list(map(int, input().split()))
block = 100

arr.sort()
idx = 0
while block >= 0:
    block -= arr[idx]
    if block < 0:
        break
    idx += 1

print(idx)