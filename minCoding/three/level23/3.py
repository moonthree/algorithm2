n = int(input())
arr = ['A', 'B', 'C']

depth = n
branch = len(arr)

path = ['']*depth

cnt = 0
def chocolet(level):
    global cnt
    if level == depth:
        cnt += 1
        return
    for i in range(branch):
        if level>1 and path[level-2] == path[level-1] == arr[i]:
            continue
        path[level] = arr[i]
        chocolet(level+1)

chocolet(0)
print(cnt)
