from collections import deque


def bfs(sty, stx, target):
    global visited
    q = deque()
    q.append([sty, stx, 0])

    visited[sty][stx] = True

    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    cnt = 1
    while q:
        now = q.popleft()
        nowy, nowx, level = now[0], now[1], now[2]
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > 3 or dx > 8:
                continue
            if visited[dy][dx] or arr[dy][dx] != target:
                continue
            visited[dy][dx] = True
            q.append([dy, dx, level+1])
            cnt += 1

    return cnt

arr = [list(map(int, input().split())) for _ in range(4)]
arr2 = sum(arr, [])
arr3 = list(set(arr2))
visited = [[False]*9 for _ in range(4)]

max_area = -21e8
max_target = 0
for i in range(4):
    for j in range(9):
        if arr[i][j] in arr3 and not visited[i][j]:
            area = bfs(i, j, arr[i][j])
            if area > max_area:
                max_area = area
                max_target = arr[i][j]

print(max_area*max_target)