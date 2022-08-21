name = ['A', 'B', 'C', 'D', 'E']

arr = [[0, 4, 0, 0, 0],
       [0, 0, 1, 2, 9],
       [5, 0, 0, 7, 0],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]
       ]

start = int(input())
cost = 0
used = [0] * 5
cost_min = int(21e8)


def dfs(now):
    global cost
    global cost_min
    if now == 4:
        if cost < cost_min:
            cost_min = cost
    for i in range(5):
        if used[i] == 0 and arr[now][i] != 0:
            cost += arr[now][i]
            used[i] = 1
            dfs(i)
            cost -= arr[now][i]
            used[i] = 0


used[start] = 1
dfs(start)

print(cost_min)
