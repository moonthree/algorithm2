win = [[3, 5, 1], [4, 2, 6]]

people = list(map(int, input().split()))

def isExist(num):
    for i in range(len(win)):
        for j in range(len(win[i])):
            if num == win[i][j]:
                return 1
                break
    return 0

for i in people:
    if isExist(i):
        print(f'{i}번 합격')
    else:
        print(f'{i}번 불합격')