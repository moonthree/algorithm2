from collections import deque

n = int(input())
virus = list(map(int, input().split()))
arr = [[0]*n for _ in range(n)]
q = deque()

for i in range(1, len(virus), 2):
    q.append([virus[i-1], virus[i], 1])

answer = 0
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

while q:
    now = q.popleft()
    nowy, nowx, level = now[0], now[1], now[2]
    arr[nowy][nowx] = level
    for i in range(4):
        dy = directy[i] + nowy
        dx = directx[i] + nowx
        if dy < 0 or dx < 0 or dy > n-1 or dx > n-1 or arr[dy][dx] != 0:
            continue
        arr[dy][dx] = level
        q.append([dy, dx, level+1])

for i in range(n):
    for j in range(n):
        print(arr[i][j],end='')
    print()