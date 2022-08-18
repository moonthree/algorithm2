name = ['B', 'A', 'C', 'D']

arr = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]

used = [0] * 4
cnt = 0
answer = []


def dfs(now):
    global cnt
    global answer
    answer.append(name[now])
    if now == 3:
        cnt += 1
        print(answer)

    for i in range(4):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)
            answer.pop()
            used[i] = 0


used[1] = 1
dfs(1)
print(cnt)
