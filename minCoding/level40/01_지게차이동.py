from collections import deque

n = 4
arr = [list(map(int, input().split())) for _ in range(n)]
acc = [[-1] * n for _ in range(n)]
acc[0][0] = 0
q = deque([(0, 0)])
directy = [1, 0]
directx = [0, 1]

while q:
    y, x = q.popleft()

    for k in range(2):
        dy = directy[k] + y
        dx = directx[k] + x

        if dy >= n or dy < 0 or dx >= n or dx < 0:
            continue

        if acc[dy][dx] == -1 or arr[dy][dx] + acc[y][x] <= acc[dy][dx]:
            acc[dy][dx] = arr[dy][dx] + acc[y][x]
        q.append([dy, dx])

directy = [-1, 0]
directx = [0, -1]
p = deque([(n - 1, n - 1)])
path = [[n - 1, n - 1]]

while p:
    y, x = p.popleft()

    for k in range(2):
        dy = directy[k] + y
        dx = directx[k] + x

        if dy >= n or dy < 0 or dx >= n or dx < 0:
            continue

        if acc[y][x] - arr[y][x] == acc[dy][dx]:
            path.append([dy, dx])
            p.append([dy, dx])

while path:
    y, x = path.pop()

    print(f'{y},{x}')
