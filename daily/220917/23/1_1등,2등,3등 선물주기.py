name = input()

used = [0]*len(name)
path = []

def dfs(level):
    if level == 3:
        for i in path:
            print(i, end='')
        print()

    for i in range(len(name)):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(name[i])
        dfs(level+1)
        path.pop()
        used[i] = 0

dfs(0)

