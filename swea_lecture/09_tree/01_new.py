def post(now):
    if now > node:
        return
    post(now * 2)
    post(now * 2 + 1)
    if now > 1:
        tree[now//2] += tree[now]

t = int(input())

for tc in range(1, t+1):
    node, leaf, target = map(int, input().split())
    tree = [0] * (node + 1)
    for i in range(leaf):
        a, b = map(int, input().split())
        tree[a] = b

    post(1)
    print(tree[target])
