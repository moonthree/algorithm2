def dfs(level):
    global MIN, total
    if level == n:
        if MIN > total:
            MIN = total
        return
    if MIN <= total:
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            total += arr[level][i]
            dfs(level+1)
            visited[i] = 0
            total -= arr[level][i]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    MIN = 21e8
    total = 0
    dfs(0)
    print(f'#{tc} {MIN}')


