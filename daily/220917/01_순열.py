dice = [1, 2, 3, 4, 5, 6]
used = [0]*6
path = []
def dfs(level):
    if level == 3:
        print(*path)
        return

    for i in range(6):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(dice[i])
        dfs(level+1)
        used[i] = 0
        path.pop()


dfs(0)
