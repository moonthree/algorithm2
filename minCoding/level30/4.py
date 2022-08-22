def bfs(start_node):
    queue = [start_node]
    used = [0] * 6
    used[start_node] = 1

    while queue:
        node = queue.pop(0)
        print(node)
        for i in range(len(arr[node])):
            if arr[node][i] == 1:
                if used[i] == 0:
                    used[i] = 1
                    queue.append(i)


arr = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]

bfs(int(input()))