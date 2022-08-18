name = ['A', 'B', 'C', 'D', 'E']

arr = [[0, 1, 0, 0, 0],
       [0, 0, 1, 1, 1],
       [1, 0, 0, 1, 0],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]
       ]
start = int(input())
cnt = 0
used = [0]*5
path = []

def dfs(now):
    global cnt
    global path
    path.append(name[now])

    if now == 4:
        cnt += 1
        for i in range(len(path)):
            print(f'{path[i]}', end=' ')
        print()


    for i in range(5):
        if used[i] == 0 and arr[now][i] == 1:
            used[i] = 1

            dfs(i)
            path.pop()
            used[i] = 0

used[start] = 1
dfs(start)

print(cnt)
