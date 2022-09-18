n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
path = []
used = [[0]*n*n]
print(used)
MAX = -21e8
def dfs(level):
    if level == n:
        print(path, end=' ')
        return

    for i in range(n):
        total = 0
        for j in range(n):
            total += arr[i][j]
        if used[i][j] == 1:
            continue
        used[i][j] = 1
        path.append(total)
        dfs(level+1)
        path.pop()
        used[i][j] = 0

dfs(0)

