name = [1, 2, 3, 4, 5, 6]

arr = [[0, 0, 1, 0, 1, 1],
       [1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]
       ]

used = [0] * 6
a, b = map(int, input().split())
short = int(21e8)
def dfs(now, level):
    global short
    if now == b-1:
        if level < short:
            short = level

    for i in range(6):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i, level+1)
            used[i] = 0


used[a-1] = 1
dfs(a-1, 0)
if short == int(21e8):
    print(0)
else:
    print(short)

