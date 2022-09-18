arr = ['A', 'B', 'C']

path = []

def dfs(level):
    if level == 2:
        for i in path:
            print(i, end='')
        print()
        return
    for i in range(len(arr)):
        path.append(arr[i])
        dfs(level+1)
        path.pop()

dfs(0)