name = list(input().split())
find = input()
arr = [[0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

answer = []
def dfs(now):
    global answer
    answer.append(name[now])
    for i in range(6):
        if arr[now][i] == 1:
            dfs(i)

dfs(0)

print(answer)