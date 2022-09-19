import copy


def dfs(now, z):
    global cnt
    global arr
    global result
    global Max

    if z == n:
        return
    if now == 3:
        for k in range(len(arr)):
            arr[k] = arr[k] * 2
        dfs(0, z + 1)
        if Max < cnt:
            Max = cnt
        return

    if now == 0:
        for i in range(0, 3):
            if i in used:
                continue
            arr_copy = copy.deepcopy(arr)
            cnt += arr[i]
            arr[i] = 0
            dfs(now + 1, z)
            arr = copy.deepcopy(arr_copy)
            cnt -= arr[i]

    elif now == 1:
        for i in range(3, 6):
            if i in used:
                continue
            arr_copy = copy.deepcopy(arr)
            cnt += arr[i]
            arr[i] = 0
            dfs(now + 1, z)
            arr = copy.deepcopy(arr_copy)
            cnt -= arr[i]

    elif now == 2:
        for i in range(1, 5):
            if i in used:
                continue
            arr_copy = copy.deepcopy(arr)
            cnt += arr[i]
            arr[i] = 0
            dfs(now + 1, z)
            arr = copy.deepcopy(arr_copy)
            cnt -= arr[i]


arr = list(map(int, input().split()))
n = int(input())
cnt = 0
result = 0
used = []
Max = 0
dfs(0, 0)
print(Max)
