from collections import deque

def water(sty, stx):
    global water_list
    q = deque()
    q.append([sty, stx, 0])
    visited = [[0] * n for _ in range(n)]
    visited[sty][stx] = 1

    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]
        if arr[nowy][nowx] == 'A':
            water_list.append([nowy, nowx, level])
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if arr[dy][dx] == '#' or arr[dy][dx] == '$' or visited[dy][dx] == 1:
                continue
            visited[dy][dx] = 1

            q.append([dy, dx, level+1])

def fire(sty, stx, level):
    global answer
    q = deque()
    q.append([sty, stx, level])
    visited = [[0] * n for _ in range(n)]
    visited[sty][stx] = 1

    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]

        if arr[nowy][nowx] == '$':
            answer = min(answer, level)
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx

            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if visited[dy][dx] == 1 or arr[dy][dx] == '#':
                continue
            visited[dy][dx] = 1
            q.append([dy, dx, level + 1])




n = int(input())
arr = [list(input()) for _ in range(n)]
y, x = map(int, input().split())
water_list = []
answer = 21e8
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]
water(y, x)
for i in water_list:
    fire(i[0], i[1], i[2])
print(answer)