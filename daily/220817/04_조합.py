# 조합
dice = [1, 2, 3, 4, 5, 6]

depth = 3
branch = 6
path = [0]*depth

def abcd(level, start):
    if level == depth:
        for i in range(depth):
            print(path[i], end='')
        print()
        return

    for i in range(start, branch):
        path[level] = dice[i]
        abcd(level+1, i+1)

abcd(0, 0)


# def abc(level):
#     if level == depth:
#         for i in range(level):
#             print(path[i], end='')
#         print()
#         return
#
#     for i in range(branch):
#         if level > 0 and path[level - 1] >= dice[i]:
#             continue
#         path[level] = dice[i]
#         abc(level+1)
#
# abc(0)
# print()