def bfs(st):
    node = [st]  # 노드 번호 넣는 큐, 시작점 넣고 시작
    visited[st] = 1  # 방문한 노드 체크

    while node:  # 큐에 노드가 있는동안
        now = node.pop()  # 맨 앞 꺼냄
        for i in range(e):
            if arr[i][0] == now and visited[arr[i][1]] == 0:  # 현재 위치를 찾고, 방문할 곳에 방문한 적이 없으면
                move = arr[i][1]  # 해당 노드로 가겠음
                node.append(move)  # 감, 큐에 방문한 노드 저장
                distance[move] = distance[now] + 1  # 움직인 거리 +1
                visited[move] = 1  # 방문 확인
            if arr[i][1] == now and visited[arr[i][0]] == 0:
                move = arr[i][0]
                node.append(move)
                distance[move] = distance[now] + 1
                visited[move] = 1


t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    visited = [0] * (v+1)
    distance = [0] * (v+1)

    bfs(s)

    if distance[g] == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {distance[g]}')