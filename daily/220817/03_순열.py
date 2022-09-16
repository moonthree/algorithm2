# 순열
dice = [1, 2, 3, 4, 5, 6]

depth = 3           # 몇 자리까지 나열할지
branch = 6          # 주사위니까 6
path = [0]*depth
used = [0]*branch   # 순열은 중복없이 선택하므로 used 사용

def abc(level):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return

    for i in range(branch):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = dice[i]
        abc(level+1)
        path[level] = 0
        used[i] = 0

abc(0)