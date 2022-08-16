n = int(input())
path = [0]*4

def clean(level):
    if level == 4:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(1, n+1):
        path[level] = i
        clean(level+1)

clean(0)