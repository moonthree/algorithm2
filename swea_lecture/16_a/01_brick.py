def police(level, y, x):
    global MAX
    arr2 = [[0]*(n*2) for _ in range(n*2)]
    arr2[y][x] = 1
    if level == n:
        return
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    sty, stx = y-level, x-level
    for i in range(sty, sty+2*level+2):
        for j in range(stx, stx+2*level+2):
            arr2[i][j] = 1


    cost = level * level + (level-1)*(level-1)
    home = 0
    t = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and arr2[i][j]:
                home += 1
            if arr2[i][j]:
                t += 1
    revenue = home * m
    print(y, x, level, home, t)
    if revenue - cost >= 0:
        MAX = max(home, MAX)
    # print(level)
    for i in range(n):
        for j in range(n):
            print(arr2[i][j], end=' ')
        print()
    print()
    #police(level+1, y, x)


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
            police(9, yy, xx)
    police(9, 9, 9)
    print(f'#{tc} {MAX}')