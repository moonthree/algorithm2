from collections import deque

def police(level, y, x):
    global MAX
    if level == n+2:
        return
    q = deque()
    q.append((level, 1, y, x))
    service = [[0]*n for _ in range(n)]
    service[y][x] = 1
    directy = [-1, 1, 0, 0, 0]
    directx = [0, 0, -1, 1, 0]

    while q:
        level, expand, nowy, nowx = q.popleft()
        if level == expand:
            break
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if service[dy][dx]:
                continue
            service[dy][dx] = 1
            q.append((level, expand+1, dy, dx))
    # for i in range(n):
    #     for j in range(n):
    #         print(visited[i][j], end=' ')
    #     print()
    home = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and service[i][j] == 1:
                home += 1
    cost = level*level + (level-1)*(level-1)
    if home*m >= cost:
        MAX = max(home, MAX)

    police(level+1, y, x)

t = int(input())

for tc in range(1, t+1):
    # 크기 : n*n
    # 비용 : m
    # 운영 비용 : 서비스 면적
    # 맵의 면적을 벗어나도 서비스 이용 비용은 줄어들지 않음
    # 정답은 손해를 보지 않으면서 홈방범 서비스를
    # 가장 많은 집들에 제공하는 서비스 영역을 찾았을 때,
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    MAX = int(-21e8)
    for yy in range(n):
        for xx in range(n):
            police(1, yy, xx)
    print(f'#{tc} {MAX}')