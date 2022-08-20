arr = [[3, 2, 4, 1],
       [0, 1, 0, 5],
       [2, 0, 3, 0],
       [5, 4, 0, 2],
       [2, -5, 0, 3]]

start = int(input())
maxi = int(-21e8)
depth = 5
branch = 4

def dfs(start, level, sums):
    global maxi
    if level == depth:
        if sums > maxi:
            maxi = sums
        return
    for i in range(start, start+3):
        if i < 0 or i > 3 or arr[level][i] == 0:
            continue
        dfs(i, level+1, sums+arr[level][i])

dfs(start, 0, 0)
print(maxi)