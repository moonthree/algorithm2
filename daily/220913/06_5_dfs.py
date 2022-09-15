# *7%10
import copy

arr = [[4, 2, 1], [5, 3, 9], [7, 8, 1]]

directy = [-1, 1, 0, 0, 0]
directx = [0, 0, -1, 1, 0]

Max = -21e8


def dfs(level):
    global Max, arr
    backup = copy.deepcopy(arr)
    if level == 3:
        ret = getSum()
        Max = max(Max, ret)
        return
    for i in range(3):
        for j in range(3):
            direct(i, j)
            dfs(level + 1)
            arr = copy.deepcopy(backup)


def direct(a, b):
    global arr
    for i in range(5):
        dy = a + directy[i]
        dx = b + directx[i]
        if dy < 0 or dx < 0 or dy > 2 or dx > 2:
            continue
        arr[dy][dx] = (arr[dy][dx] * 7) % 10
    # return


def getSum():
    ssum = 0
    for i in range(3):
        for j in range(3):
            ssum += arr[i][j]
    return ssum


dfs(0)
print(Max)
