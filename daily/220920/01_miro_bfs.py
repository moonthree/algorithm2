from collections import deque
# 배열 범위
# 벽x
# 중복체크
def bfs(y, x, level):
    global feed, feed_idx
    q = deque()
    q.append([y, x, level])
    while q:
        nowy, nowx, level = q.popleft()
        visited[nowy][nowx] = 1
        feed = level
        feed_idx = [nowy, nowx]
        if arr[nowy][nowx] == 8:
            break
        directy = [-1, 1, 0, 0]
        directx = [0, 0, -1, 1]

        for i in range(4):
            dy = nowy+directy[i]
            dx = nowx+directx[i]
            if dy < 0 or dx < 0 or dy > 3 or dx > 4:
                continue
            if visited[dy][dx] == 1 or arr[dy][dx] == 1:
                continue
            q.append([dy, dx, level+1])

def target(y, x, level):
    global meet
    q2 = deque()
    q2.append([y, x, level])
    while q2:
        nowy, nowx, level = q2.popleft()
        visited2[nowy][nowx] = 1
        meet = level
        if arr[nowy][nowx] == 9:
            break
        directy = [-1, 1, 0, 0]
        directx = [0, 0, -1, 1]

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > 3 or dx > 4:
                continue
            if visited2[dy][dx] == 1 or arr[dy][dx] == 1:
                continue
            q2.append([dy, dx, level + 1])

arr = [[0, 0, 0, 1, 1],
       [0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0],
       [8, 0, 0, 0, 9]]

visited = [[0]*5 for _ in range(4)]
visited2 = [[0]*5 for _ in range(4)]

feed = 0
feed_idx = [0, 0]
meet = 0

bfs(0, 0, 0)
target(feed_idx[0], feed_idx[1], 0)

print(feed+meet)