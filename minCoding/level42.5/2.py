import copy
arr = [list(input()) for _ in range(4)]
n = int(input())

directy = [-1, 1, 0, 0, 0]
directx = [0, 0, -1, 1, 0]
Max = -21e8
path = []
result = []
def dfs(level):
    global Max, arr, result
    backup = copy.deepcopy(arr)
    if level == n:
        ret = getSum()
        if ret > Max:
            Max = ret
            for i in range(level):
                result = path[:]
        return
    for y in range(4):
        for x in range(4):
            if arr[y][x] != '_':
                bomb(y, x)
                path.append(backup[y][x])
                dfs(level+1)
                path.pop()
                arr = copy.deepcopy(backup)

def getSum():
    ssum = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] == '_':
                ssum += 1
    return ssum

def bomb(a, b):
    global arr
    for i in range(5):
        dy = a + directy[i]
        dx = b + directx[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        arr[dy][dx] = '_'

dfs(0)
result.sort()
print(*result)