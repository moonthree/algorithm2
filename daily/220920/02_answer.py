from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    size = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if Map[ny][nx] == 1:
                    q.append([ny, nx])
                    Map[ny][nx] = 0
                    size += 1
    return size

Map = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

for y in range(5):
    for x in range(5):
        if Map[y][x] == 1:
            print(bfs(y, x))