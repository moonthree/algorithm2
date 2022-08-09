arr = [3, 7, 4, 1, 2, 6]

univer = [list(map(int, input().split())) for _ in range(2)]

def isExist(element):
    a = False
    for i in arr:
        if i == element:
            a = True
    if a:
        return 'OK'
    else:
        return 'NO'


for i in range(len(univer)):
    for j in range(len(univer[i])):
        print(isExist(univer[i][j]), end=' ')
    print()