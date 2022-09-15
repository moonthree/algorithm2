

def dfs(level, total):
    global cnt
    if level == n:
        if total == 10:
            cnt += 1
        return
    for i in range(1, 10):
        dfs(level+1, total+i)

cnt = 0
n = int(input())

dfs(0, 0)
print(cnt)