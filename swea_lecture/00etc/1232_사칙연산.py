def post(now):
    if tree[now] not in '*/+-':
        return tree[now]
    else:
        left_result = float(post(left_child[now]))
        right_result = float(post(right_child[now]))
        if tree[now] == '*':
            return left_result * right_result
        elif tree[now] == '/':
            return left_result / right_result
        elif tree[now] == '+':
            return left_result + right_result
        elif tree[now] == '-':
            return left_result - right_result


for tc in range(1, 11):
    n = int(input())
    left_child = [0] * (n + 1)
    right_child = [0] * (n + 1)
    tree = [''] * (n + 1)

    for i in range(n):
        data = list(input().split())
        if len(data) == 2:                  # 자식이 없는 경우, 단말 노드, 피연산자
            tree[int(data[0])] = data[1]
        else:                               # 자식이 있는 경우, 연산자
            tree[int(data[0])] = data[1]
            left_child[int(data[0])] = int(data[2])
            right_child[int(data[0])] = int(data[3])

    result = post(1)
    print(f'#{tc} {int(result)}')

