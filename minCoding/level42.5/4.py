import copy
n = int(input())
arr = list(map(int, input().split()))
path = []
result = []
Max = -21e8
def dfs(level, total):
    global arr, path, Max, result
    temp = copy.deepcopy(arr)
    if level == n:
        if total > Max:
            Max = total
            #print(total)
            #print(path)
            for i in range(level):
                result = path[:]
        return
    for i in range(n):
        path.append(arr[i])
        shot(i)
        dfs(level+1, total + temp[i])
        path.pop()
        arr = copy.deepcopy(temp)

def shot(i):
    global arr
    if i == 0:
        arr[i], arr[i+1] = 0, 0
    elif i == n-1:
        arr[i], arr[i-1] = 0, 0
    else:
        arr[i-1], arr[i], arr[i+1] = 0, 0, 0

dfs(0, 0)
result2 = []
for i in result:
    if i != 0:
        result2.append(i)
for i in range(len(result2)-1):
    print(f'{result2[i]}+', end='')
print(f'{result2[-1]}={sum(result2)}')