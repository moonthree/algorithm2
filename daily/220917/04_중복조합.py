arr = ['a', 'b', 'c', 'd']

n = 3
path = []
def dfs(level, start):
    if level == n:
        print(*path)
        return

    for i in range(start, 4):
        path.append(arr[i])
        dfs(level+1, i)
        path.pop()


dfs(0,0)