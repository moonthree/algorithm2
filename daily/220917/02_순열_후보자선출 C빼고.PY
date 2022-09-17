candy = ['A', 'B', 'C', 'D']

n = 3
used = [0]*4
path = []

def dfs(level):
    if level == 1 and path[0] == 'C':
        return

    if level == 3:
        # if path[0] != 'C':
        print(*path)
        return

    for i in range(len(candy)):
        # if used[i] == 1 or (candy[i] == 'C' and level == 0):
        #     continue
        path.append(candy[i])
        used[i] = 1
        dfs(level+1)
        path.pop()
        used[i] = 0

dfs(0)