def dfs(start_node):
    stack = [start_node]
    used = []

    while stack:
        node = stack.pop()
        if node not in used:
            used.append(node)
            for i in range(len(arr[node])-1, -1, -1):
                if arr[node][i] == 1:
                    stack.append(i)
    print(*used)


arr = [
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

dfs(int(input()))