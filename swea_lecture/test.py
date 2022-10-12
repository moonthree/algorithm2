n = 2
arr = [[0]*2 for _ in range(n)]
cnt = 0
def dfs(level):
    global cnt
    if level == 2:
        cnt += 1
        print(cnt,'번')
        for i in range(n):
            print(*arr[i])
        print()
        return

    for j in range(n):
        for i in range(n):
            if arr[j][i] == 0:
                arr[j][i] = 1
                dfs(level+1)
                arr[j][i] = 0

dfs(0)