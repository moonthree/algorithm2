name = ['B', 'A', 'C', 'D']
arr = [
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]
answer = []
used = [0] * 4


def dfs(now):
    global answer
    answer.append(name[now])
    for i in range(4):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)


used[2] = 1
dfs(2)

print(answer)
