from collections import deque

def bfs(start_node):
    q = deque()
    q.append(start_node)
    used = [0] * 4

    while q:
        node = q.popleft()
        print(name[node])
        for i in range(4):
            if arr[start_node][i] == 1:
                if used[i] == 0:
                    used[i] = 1
                    q.append(i)


name = ['A', 'B', 'C', 'D']
arr = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

bfs(1)