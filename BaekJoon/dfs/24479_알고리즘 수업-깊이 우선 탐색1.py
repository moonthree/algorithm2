import sys
input = sys.stdin.readline

def dfs(arr, v, used):
    global path
    used[v] = True

    for i in range(len(arr[v])):
        #path[i] = 0
        if arr[v][i] == 1 and not used[i]:
            path[i] = v
            dfs(arr, i, used)


n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
used = [False]*(n+1)
path = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b], arr[b][a] = 1, 1

dfs(arr, v, used)

print(path)
