def bfs(s, g):
    queue = [s]
    while queue:
        now = queue.pop(0)
        for i in arr[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1
    if visited[g] - 1 < 0:
        return 0
    return visited[g] - 1


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a - 1].append(b - 1)
        arr[b - 1].append(a - 1)

    s, g = map(int, input().split())
    visited = [0] * (v+1)
    visited[s-1] = 1

    print(f'#{tc} {bfs(s-1, g-1)}')