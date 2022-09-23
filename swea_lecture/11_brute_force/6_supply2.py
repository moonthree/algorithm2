from collections import deque
def bfs():
    global MIN
    q = deque()
    q.append((0, 0))
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    visited = [[False]*n for _ in range(n)]
    visited[0][0] = True
    time = [[0] * n for _ in range(n)]

    while q:
        ny, nx = q.popleft()
        for i in range(4):
            dy = ny + directy[i]
            dx = nx + directx[i]
            if 0 <= dy < n and 0 <= dx < n:
                if dy == 0 and dx == 0:
                    continue
                elif not visited[dy][dx]:
                    visited[dy][dx] = True
                    time[dy][dx] = time[ny][nx] + arr[dy][dx]
                    q.append((dy, dx))
                else:
                    if time[dy][dx] > time[ny][nx] + arr[dy][dx]:
                        time[dy][dx] = time[ny][nx] + arr[dy][dx]
                        q.append((ny, nx))
    return time[n-1][n-1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ans = bfs()
    print(f'#{tc} {ans}')