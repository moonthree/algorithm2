import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for i in graph[now]:
            cost = i[1] + dis
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

t = int(input())

for tc in range(1, t+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    INF = int(21e8)
    distance = [INF]*(n+1)

    for i in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(0)
    print(f'#{tc} {distance[n]}')

