import heapq

n, m, x = map(int, input().split())  # 노드, 간선, 시작

INF = int(21e8)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [INF] * (n + 1)
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

    return distance
arr2 = []
bucket = [0]*(n+1)
for i in range(1, n+1):
    a = dijkstra(i)
    if i != x:
        bucket[i] += a[x]
    elif i == x:
        for j in range(len(a)):
            bucket[j] += a[j]

new_bucket = []
for i in bucket:
    if i < INF:
        new_bucket.append(i)

print(max(new_bucket))

