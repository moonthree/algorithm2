import sys
input = sys.stdin.readline

def dfs(arr, v, used):
    used[v] = True

    for i in range(len(arr[v])):
        if arr[v][i] == 1 and not used[i]:
            dfs(arr, i, used)
            path[i] = v


n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
used = [False]*(n+1)
path = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b], arr[b][a] = 1, 1

dfs(arr, v, used)

print(path)