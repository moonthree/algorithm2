from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    acc = [[-1] * N for _ in range(N)]
    sy, sx, ey, ex = 0, 0, N - 1, N - 1
    acc[sy][sx] = 0
    q = deque([(sy, sx)])
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= N or dx < 0:
                continue
            if acc[dy][dx] != -1 and acc[dy][dx] <= arr[dy][dx] + acc[y][x]:
                continue
            acc[dy][dx] = acc[y][x] + arr[dy][dx]
            q.append([dy, dx])

    print(f'#{tc} {acc[ey][ex]}')