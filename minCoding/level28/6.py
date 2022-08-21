word = input()

arr = [list(map(int, input().split())) for _ in range(len(word))]

def dfs(now):
    print(word[now], end='')
    for i in range(len(arr)):
        if arr[now][i] == 1:
            dfs(i)

dfs(0)