arr = [3, 4, 5, 1, 6, 9]

# 조합
n = 3
Max = -21e8
def dfs(level, total, start):
    global Max
    if level == n:
        Max = max(total, Max)
        return

    for i in range(start, 6):
        dfs(level+1, total+arr[i], i+1)

dfs(0, 0, 0)

print(Max)


# 순열
Max2 = -21e8
used2 = [0]*6
def dfs2(level, total):
    global Max2
    if level == n:
        Max2 = max(total, Max2)
        return
    for i in range(6):
        if used2[i] == 1:
            continue
        used2[i] = 1
        dfs2(level+1, total+arr[i])
        used2[i] = 0

dfs2(0, 0)
print(Max2)