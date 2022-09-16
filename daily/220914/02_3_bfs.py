from collections import deque

n = int(input())  # map 사이즈 입력
y, x = map(int, input().split())  # 시작점 입력
arr = [[0] * n for _ in range(n)]

arr[y][x] = 1
q = deque()
q.append([y, x])

while q:
    now = q.popleft()
    y, x = now[0], now[1]
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if 0 <= dy < n and 0 <= dx < n:  # 배열범위
            if arr[dy][dx] == 0:  # 이미 꽃이 안핀 곳이라면
                arr[dy][dx] = arr[y][x] + 1
                q.append([dy, dx])

for i in arr:
    print(*i)