# 중복조합
dice = [1, 2, 3, 4, 5, 6]

depth = 3
branch = 6
path = [0]*depth



def abc(level, start):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return

    for i in range(start, branch):
        path[level] = dice[i]
        abc(level+1, i)

abc(0, 0)
print()