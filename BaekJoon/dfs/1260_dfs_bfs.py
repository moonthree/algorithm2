from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in range(len(graph[v])):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

def bfs(start_node):
    q = deque([start_node])

    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and not used[i]:
                used[i] = True
                q.append(i)


n, m, v = map(int, input().split())
visited = [False]*(n+1)
used = [False]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a][b], graph[b][a] = 1, 1

dfs(graph, v, visited)
print()
used[v] = True
bfs(v)