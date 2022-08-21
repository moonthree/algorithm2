n = int(input())
dice = [1, 2, 3, 4, 5, 6]
path = [0]*n
def abc(level):
    if level == n:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(len(dice)):
        path[level] = dice[i]
        abc(level+1)
abc(0)