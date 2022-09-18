n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
path = []
used = [[0]*n]*n
used2 = [0]*n
MAX = -21e8
def dfs(level, total):
    if level == n:
        print(*path, end=' ')
        print(':', end=' ')
        print(total, end='')
        print()
        return
    for i in range(n):
        for j in range(n):
            if used[i] == 1:
                continue
            path.append(arr[i][j])
            used[i] = 1
            dfs(level+1, total+arr[i][j])
            used[i] = 0
            path.pop()

dfs(0, 0)

