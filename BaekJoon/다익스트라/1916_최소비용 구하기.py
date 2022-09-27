import heapq

n = int(input()) # 노드
m = int(input()) # 간선

INF = int(21e8)
graph = [[] for _ in range(n+1)]
result = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

st, ed = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0

    while q:
        dis, now = heapq.heappop(q)
        if result[now] < dis:
            continue
        for i in graph[now]:
            cost = i[1] + dis
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(st)
print(result[ed])