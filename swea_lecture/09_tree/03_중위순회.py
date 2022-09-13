def inorder(now):
    if now > n:
        return
    inorder(now * 2)
    print(tree[now], end='')
    inorder(now * 2 + 1)

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n+1)
    for i in range(1, n+1):
        arr = list(input().split())
        tree[i] = arr[1]
    print(f'#{tc}', end=' ')
    inorder(1)
    print()
