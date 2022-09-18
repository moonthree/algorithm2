arr = ['A', 'B', 'C', 'D']

n = 3
word = list(input())
cnt = 1
path = []
def dfs(level):
    global cnt
    if level == n:
        if path == word:
            print(f'{cnt}번째')
        cnt += 1
        return
    for i in range(4):
        path.append(arr[i])
        dfs(level+1)
        path.pop()

dfs(0)