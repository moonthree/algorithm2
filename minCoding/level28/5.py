n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
path = []
level = 0
def dfs(now):
    global level
    path.append(now)
    if level == 2:
        for i in path:
            print(i, end=' ')
        print()

    for i in range(len(arr)):
        if arr[now][i] == 1:
            level += 1
            dfs(i)
            path.pop()
            level -= 1

dfs(0)