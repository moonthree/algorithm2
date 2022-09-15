n = input()

depth = 3
branch = len(n)
path = [0]*depth


def abc(level, start):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return

    for i in range(start, branch):
        path[level] = n[i]
        abc(level+1, i)

abc(0, 0)
print()