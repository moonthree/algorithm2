from collections import deque

# 00 01 02
# 10 11 12
# 20 21 22

arr = [list(map(int, input().split())) for _ in range(4)]

q = deque()
answer = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            q.append([i, j, 0])

visited = [[0]*5 for _ in range(4)]

while q:
    now = q.popleft()
    nowy, nowx, level = now[0], now[1], now[2]
    answer = level
    visited[nowy][nowx] = 1
    directy = [-1, 1, 0, 0, -1, -1, 1, 1]
    directx = [0, 0, -1, 1, -1, 1, 1, -1]
    for i in range(8):
        dy = directy[i] + nowy
        dx = directx[i] + nowx

        if dy < 0 or dx < 0 or dy > 3 or dx > 4 or visited[dy][dx] == 1:
            continue
        visited[dy][dx] = 1
        q.append([dy, dx, level+1])


print(answer)