# 중복순열
dice = [1, 2, 3, 4, 5, 6]

depth = 3
branch = 6
path = [0]*depth

def abc(level):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return

    for i in range(branch):
        path[level] = dice[i]
        abc(level+1)
        path[level] = 0

abc(0)