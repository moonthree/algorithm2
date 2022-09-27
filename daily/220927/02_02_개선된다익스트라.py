import heapq

n, m = map(int, input().split())            # 노드의 개수, 간선의 개수 입력받기
st, ed = map(int, input().split())          # 시작 노드, 도착 노드

INF = int(21e8)
graph = [[] for _ in range(n+1)]            # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
distance = [INF] * (n+1)                    # 최단거리테이블을 모두 무한으로 초기화

for _ in range(m):                          # 모든 간선정보를 입력받기
    a, b, c = map(int, input().split())     # a = 출발, b = 도착, c = 비용
    graph[a].append((b, c))                 # a에서부터 b까지 가는 거리가 c다

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))        # 시작 노드는 본인이므로 비용 0으로 큐에 삽입
    distance[start] = 0

    while heap:                             # 큐가 빌때까지
        dist, now = heapq.heappop(heap)     # 거리가 가장

        if distance[now] < dist:            # 현재 노드가 이미 처리된 적 있으면 무시
            continue                        # 현재 꺼낸 그 원소의 거리값(dist)이 테이블에 기록되어 있는 값보다 더 크다면 이미 처리된 것_
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:       # 현재노드를 거쳐가는 것과 기존의 값을 비교교
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
dijkstra(st)
print(distance)
print(distance[ed])

# 5 7
# 0 3
# 0 1 3
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1