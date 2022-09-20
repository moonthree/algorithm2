from collections import deque

arr = [
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

answer = 0


def bfs(st_y, st_x, ed_y, ed_x):
    q = deque()
    q.append([st_y, st_x, 0])
    used = [[False] * 5 for _ in range(4)]
    used[st_y][st_x] = True
    while q:
        node = q.popleft()
        yy, xx, level = node[0], node[1], node[2]
        if yy == ed_y and xx == ed_x:
            return level
        for i in range(4):
            nx = dx[i] + yy
            ny = dy[i] + xx
            if not (0 <= nx < 4 and 0 <= ny < 5): continue
            if used[nx][ny] == True: continue
            if arr[nx][ny] == 1: continue
            q.append([nx, ny, level + 1])


answer += bfs(0, 0, 3, 0)
answer += bfs(3, 0, 3, 4)
print(answer)
