from collections import deque

n = int(input())
arr = [[0]*n for _ in range(n)]

q = deque()
for _ in range(2):
    y, x = map(int, input().split())
    arr[y][x] = 1
    q.append([y, x])

while q:
    now = q.popleft()
    print(q)
    y, x = now[0], now[1]
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        # print(dy, dx)
        if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
            continue
        if arr[dy][dx] == 0:
            arr[dy][dx] = arr[y][x] + 1
            q.append([dy, dx])

print(max(max(arr)))