n = int(input())
arr = list(map(int, input().split()))
cnt = 0
def a1(a, b):
    return (a-b) * (a+b)
def a2(a, b):
    return max(a, b)
def a3(a, b):
    return (a**2) - (b**2)
def a4(a, b):
    return (a+b) ** 2


def dfs(level, total):
    global cnt
    if level == n-1:
        if total == 100:
            cnt += 1
        return
    for i in range(4):
        if i == 0:
            dfs(level + 1, a1(total, arr[level+1]))
        elif i == 1:
            dfs(level + 1, a2(total, arr[level + 1]))
        elif i == 2:
            dfs(level + 1, a3(total, arr[level + 1]))
        elif i == 3:
            dfs(level + 1, a4(total, arr[level + 1]))


dfs(0, arr[0])
print(cnt)