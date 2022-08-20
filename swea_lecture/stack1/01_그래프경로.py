t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[0] * v for _ in range(v)]

    for _ in range(e):
        y, x = map(int, input().split())
        arr[y-1][x-1] = 1

    s, g = map(int, input().split())

    used = [0]*v
    cnt = 0

    def dfs(now):
        global cnt
        if now == g-1:
            cnt += 1
        for i in range(v):
            if arr[now][i] == 1 and used[i] == 0:
                used[i] = 1
                dfs(i)
                used[i] = 0

    used[s-1] = 1
    dfs(s-1)
    if cnt:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')