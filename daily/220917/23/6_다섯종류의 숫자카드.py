arr = list(input())

branch = 5
depth = 4

path = [0]*depth

cnt = 0

def card(level):
    global cnt
    if level == depth:
        cnt += 1
        return

    for i in range(branch):
        if level > 0 and abs(path[level - 1] - int(arr[i])) > 3:
            continue
        path[level] = int(arr[i])
        card(level + 1)

card(0)
print(cnt)