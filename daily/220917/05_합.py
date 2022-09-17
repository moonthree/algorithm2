arr = [3, 4, 5, 1, 6, 9]

n = int(input())

def dfs(level, total):

    if level == n:
        print(total)
        return

    # for i in range(6):
    if level != 0:
        print(total, end=' ')
    dfs(level+1, total+arr[level])

dfs(0, 0)