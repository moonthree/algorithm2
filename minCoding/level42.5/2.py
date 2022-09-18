import copy
arr = [list(input()) for _ in range(4)]
n = int(input())
used = [[0]*4 for _ in range(4)]
directy = [-1, 1, 0, 0, 0]
directx = [0, 0, -1, 1, 0]
Max = -21e8
path = []
result = []
def dfs(level, total):
    global Max, arr, result, used
    backup = copy.deepcopy(arr)
    used_backup = copy.deepcopy(used)
    if level == n:

        #return
        if total > Max:
            Max = total
            for i in range(level):
                result = path[:]
        return
    for y in range(4):
        for x in range(4):
            if arr[y][x] != '_':
                plus = bomb(y, x)
                path.append(backup[y][x])
                dfs(level+1, total+plus)
                path.pop()
                arr = copy.deepcopy(backup)
                used = copy.deepcopy(used_backup)

def bomb(a, b):
    global arr
    cnt = 0
    for i in range(5):
        dy = a + directy[i]
        dx = b + directx[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3 \
                or used[dy][dx] == 1 or arr[dy][dx] == '_':
            continue
        used[dy][dx] = 1
        cnt += 1
    arr[a][b] = '_'
    # for i in range(4):
    #     for j in range(4):
    #         print(used[i][j], end=' ')
    #     print()
    # print('_________', a, b)
    return cnt

dfs(0, 0)
result.sort()
print(*result)