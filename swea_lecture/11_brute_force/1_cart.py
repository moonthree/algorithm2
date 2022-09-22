def dfs(level):
    global Sum, Min, path
    if level == n-1:
        Sum = 0
        for i in range(1, len(path)):
            Sum += arr[path[i - 1]][path[i]]
        Sum += arr[path[len(path) - 1]][0]
        if Min > Sum:
            Min = Sum
        return
    for i in range(1, n):
        if used[i] == 1:
            continue
        path.append(i)
        used[i] = 1
        dfs(level + 1)
        used[i] = 0
        path.pop()

t= int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    used = [False]*n
    Sum = 0
    Min = 21e8
    path = [0]
    dfs(0)
    print(f'#{tc} {Min}')
