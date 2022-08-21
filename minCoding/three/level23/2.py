depth = 4
branch = 4

path = ['']*depth

arr = list(input())
cnt = 0
def bt(level):
    global cnt
    if level == depth:
        cnt += 1
        return
    for i in range(branch):
        if level > 0 and (path[level-1] == 'B' and arr[i] == 'T') or (path[level-1] == 'T' and arr[i] == 'B'):
            continue
        path[level] = arr[i]
        bt(level+1)

bt(0)

print(cnt)