import heapq

v, e = map(int, input().split())    # 노드 / 간선
st = int(input())                   # 시작점

INF = int(21e8)
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a, b, c = map(int, input().split()) # a = 출발, b = 도착, c = 비용
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(st)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
