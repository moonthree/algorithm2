arr = ['A', 'B', 'C']
depth = 2
path = ['']*4

def tree(level):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(len(arr)):
        path[level] = arr[i]
        tree(level+1)
tree(0)