arr = list(input())
depth = int(input())
path = ['']*depth

def abc(level):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(len(arr)):
        path[level] = arr[i]
        abc(level+1)

abc(0)