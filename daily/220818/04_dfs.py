# kfcdmga
words = list(input().split())
arr = [[0, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]]

answer = []
def dfs(start):
    global answer
    answer.append(words[start])
    for i in range(7):
        if arr[start][i] == 1:
            dfs(i)
dfs(0)

print(answer)