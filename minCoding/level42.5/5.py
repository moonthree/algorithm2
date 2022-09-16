import random, copy

arr = list(map(int, input().split()))
n = int(input())
path = []
def eagle1(i):
    global arr
    idx = i
    if i > 2:
        idx = random.randrange(0, 1)
    b = arr[idx]
    arr[idx] = 0
    return b
def eagle2(i):
    global arr
    idx = i
    if i < 3:
        idx = random.randrange(3, 5)
    b = arr[idx]
    arr[idx] = 0
    return b
def eagle3(i):
    global arr
    idx = i
    if i > 4 or i < 1:
        idx = random.randrange(1, 4)
    b = arr[idx]
    arr[idx] = 0
    for j in range(len(arr)):
        arr[j] = arr[j] * 2
    return b

def dfs(level, total):
    global arr
    temp = copy.deepcopy(arr)
    if level == n:
        print(path)
        return

    for i in range(6):
        dfs(level + 1, (total + eagle1(i)))
        dfs(level + 1, (total + eagle2(i)))
        dfs(level + 1, (total + eagle3(i)))
        arr = copy.deepcopy(temp)

dfs(0,0)