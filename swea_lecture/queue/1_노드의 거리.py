def bfs(v):  # 노드1
    q = []  # 노드 번호만 넣는 큐
    q.append(v)  # 노드1
    visited[v] = True
    while q:  # 큐가 빌 때까지
        v = q.pop(0)  # 앞부터 pop
        for i in range(E):  # 방향성 없기 때문, 노드 앞 뒤 다 검사하자
            if node_to_node[i][0] == v and visited[node_to_node[i][1]] == False:  # 앞
                val = node_to_node[i][1]
                q.append(val)  # 앞 맞으면 뒤노드를 큐 넣기
                distance[val] = distance[v] + 1  # 연결노드 다음이므로 +1
                visited[val] = True

            if node_to_node[i][1] == v and visited[node_to_node[i][0]] == False:  # 뒤
                val = node_to_node[i][0]
                q.append(val)  # 뒤 맞으면 앞노드를 큐 넣기
                distance[val] = distance[v] + 1
                visited[val] = True


for testCase in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    node_to_node = [list(map(int, input().split())) for _ in range(E)]
    # print(node_to_node) # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    start, end = map(int, input().split())  # 노드1 => 노드6

    visited = [False] * (V + 1)  # 번호별 방문
    distance = [0] * (V + 1)  # 번호별 도달거리
    bfs(start)  # 시작점부터 출발 # 노드1부터 시작

    print(f"#{testCase}", distance[end])  # 도착점의 도달거리
