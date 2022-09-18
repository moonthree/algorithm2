
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
def dice(i):
    global arr
    for j in range(1, n-1):
        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
    arr[i][0], arr[i][n - 1] = arr[i][n - 1], arr[i][0]

Max = -21e8
def dfs(level):
    global arr, Max
    if level == n*2:
        ret = getSum()
        Max = max(Max, ret)
        return
    for i in range(n):
        dice(i)
        dfs(level+1)

def getSum():
    total = 1
    for x in range(n):
        Sum = 0
        for y in range(n):
            Sum += arr[y][x]
        total *= Sum
    return total

dfs(0)
print(f'{Max}점')