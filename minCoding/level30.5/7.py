def recur(level, ssum):
    global cnt
    if 10 <= ssum <= 20:
        cnt += 1

    if level == len(arr):
        return

    for i in range(len(arr)):
        if level > 0 and path[level - 1] >= arr[i]:
            continue
        path[level] = arr[i]
        recur(level+1, ssum + arr[i])
        path[level] = 0


arr = list(map(int, input().split()))
path = [0]*len(arr)
cnt = 0
recur(0, 0)
print(cnt)