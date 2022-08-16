n = int(input())
path = [0]*n
dice = [1, 2, 3, 4, 5, 6]
used = [0]*6
def abc(level):
    if level == n:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return

    for i in range(len(dice)):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = dice[i]
        abc(level+1)
        used[i] = 0
        path[level] = 0

abc(0)