n, m = map(int, input().split())
arr = list(map(int, input().split()))

Min = 21e8
path = [0]*m
used = [0]*n
arr2 = []
def dfs(level, total):
    global path, used, Min, arr2
    if level == m:
        if total < Min:
            Min = total
            arr2 = path
            print(path)
        return

    for i in range(n):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = arr[i]
        dfs(level+1, total * arr[i])
        used[i] = 0


dfs(0, 1)
print(Min)
print(arr2)