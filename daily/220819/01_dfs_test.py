arr = [[2, 5, 7],
       [8, 4, -8],
       [-7, 1, 4],
       [5, 1, 9]
       ]

maxi = int(-21e8)
depth = 4
branch = 3

def dfs(level, sums):
    global maxi
    if level == 4:
        if sums > maxi:
            maxi = sums
        return

    for i in range(branch):
        dfs(level+1, sums+arr[level][i])


dfs(0, 0)
print(maxi)