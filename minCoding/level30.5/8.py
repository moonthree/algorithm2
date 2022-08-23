arr = ['B', 'I', 'A', 'H']
N = int(input())
idx = 0

for i in range(4):
    idx -= 1
    for j in range(N):
        idx += 1
    idx = idx % len(arr)
    print(arr.pop(idx), end=' ')


# n = int(input()) # 5
# arr = ['B', 'I', 'A', 'H']
# idx = 0
# while arr:
#     selected = n % len(arr)
#     idx = idx + selected - 1
#     hero = arr[idx]
#     print(hero, end=' ')
#     arr.pop(idx)