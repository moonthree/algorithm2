depth = 2
branch = 3
arr = ['a', 'b', 'c']
path = ['']*5


def tree(level):
    global path
    if depth == level:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(branch):
        path[level] = arr[i]
        tree(level+1)
tree(0)