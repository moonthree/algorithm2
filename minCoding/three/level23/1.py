# path
# used

arr = list(input())

depth = 3
branch = 4

path = ['']*depth
used = [0]*branch

def func(level):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return

    for i in range(branch):
        if used[i] == 1:
            continue
        path[level] = arr[i]
        used[i] = 1
        func(level + 1)
        used[i] = 0

func(0)