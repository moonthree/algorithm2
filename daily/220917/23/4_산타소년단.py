arr = ['B', 'T', 'S', 'K', 'R']

n = int(input())

path = []
used = [0]*len(arr)
cnt = 0
def recur(level):
    global cnt
    if level == n:
        if 'S' in path:
            cnt += 1
        return

    for i in range(5):
        if used[i] == 1:
            continue
        used[i] = 1
        path.append(arr[i])
        recur(level+1)
        path.pop()
        used[i] = 0

recur(0)
print(cnt)