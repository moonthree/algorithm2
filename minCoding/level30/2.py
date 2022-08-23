def dfs(start_node):
    stack = [start_node]
    used = []
    ssum = 0
    ssum_arr = [0]

    while stack:
        node = stack.pop()
        node2 = ssum_arr.pop()
        if node not in used:

            used.append(node)
            print(node, end=' ')
            ssum += node2
            print(ssum)
            for i in range(len(arr[node])-1, -1, -1):
                if arr[node][i] != 0:
                    stack.append(i)
                    ssum_arr.append(arr[node][i])


arr = [
    [0, 0, 1, 0, 2, 0],
    [5, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 7],
    [2, 0, 0, 0, 8, 0],
    [0, 0, 9, 0, 0, 0],
    [4, 0, 0, 7, 0, 0]
]

dfs(int(input()))