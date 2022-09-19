import copy

arr = list(map(int, input().split()))
n = int(input())
MAX = -21e8

def eagle(level, eat, total):
    global arr
    if eat == 0:
        for i in range(0, 3):
            temp = copy.deepcopy(arr)
            arr[i] = 0
            dfs(level, eat+1, total+temp[i])
            arr = copy.deepcopy(temp)
    elif eat == 1:
        for i in range(3, 6):
            temp = copy.deepcopy(arr)
            arr[i] = 0
            dfs(level, eat + 1, total + temp[i])
            arr = copy.deepcopy(temp)
    else:
        for i in range(1, 5):
            temp = copy.deepcopy(arr)
            arr[i] = 0
            dfs(level, eat + 1, total + temp[i])
            arr = copy.deepcopy(temp)


def dfs(level, eat, total):
    global MAX

    if level == n:
        MAX = max(total, MAX)
        return

    if eat == 3:
        for i in range(len(arr)):
            arr[i] = arr[i] * 2
        dfs(level+1, 0, total)
        return

    eagle(level, eat, total)

dfs(0, 0, 0)
print(MAX)