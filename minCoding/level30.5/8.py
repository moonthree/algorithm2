arr = ['B', 'I', 'A', 'H']
N = int(input())
idx = 0

for i in range(4):
    idx -= 1
    for j in range(N):
        idx += 1
    idx = idx % len(arr)
    print(arr.pop(idx), end=' ')