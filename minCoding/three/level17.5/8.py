maps = [[3, 55, 42], [-5, -9, -10]]

pix = [list(map(int, input().split())) for _ in range(2)]

def isExist(color):
    color_is = False
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if color == maps[i][j]:
                color_is = True

    if color_is:
        return 'Y'
    else:
        return 'N'

for i in range(len(pix)):
    for j in range(len(pix[i])):
        print(isExist(pix[i][j]), end=' ')
    print()