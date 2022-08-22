def dfs(start_node):
    stack = [start_node]
    used = []
    ssum = 0
    a = [0]

    while stack:
        node = stack.pop()
        node2 = a.pop()
        if node not in used:
            used.append(node)
            print(node, end=' ')
            ssum += node2
            print(ssum)
            for i in range(len(arr[node])-1, -1, -1):
                if arr[node][i] != 0:
                    stack.append(i)
                    a.append(arr[node][i])
                    # a.append(i)
                    # print(a)



arr = [
    [0, 0, 1, 0, 2, 0],
    [5, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 7],
    [2, 0, 0, 0, 8, 0],
    [0, 0, 9, 0, 0, 0],
    [4, 0, 0, 7, 0, 0]
]

dfs(int(input()))