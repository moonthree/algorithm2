# 산타소년단
# S 필수포함
# path, used

n = int(input())
arr = ['B', 'T', 'S', 'K', 'R']

branch = len(arr)
depth = n

path = ['']*depth
used = [0]*branch

cnt = 0
def sts(level):
    global cnt
    if level == depth:
        for i in range(level):
            if path[i] == 'S':
                cnt += 1
        return

    for i in range(branch):
        if used[i] == 1:
            continue
        path[level] = arr[i]
        used[i] = 1
        sts(level+1)
        used[i] = 0
sts(0)
print(cnt)
