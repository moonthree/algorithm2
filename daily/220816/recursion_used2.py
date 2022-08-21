depth = 3
arr = ['a', 'b', 'c', 'd']

path = ['']*3
used = [0]*4

def abc(level):
    if level == depth:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(4):
        if used[i] == 1:
            continue
        path[level] = arr[i]
        used[i] = 1
        abc(level+1)
        used[i] = 0

abc(0)