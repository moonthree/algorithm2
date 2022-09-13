t = int(input())

for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)

    for i in range(m):
        idx, val = map(int, input().split())
        tree[idx] = val
    def post(now):
        if now > n:
            return
        post(now * 2)
        post(now * 2 + 1)
        if now > 1:
            tree[now//2] += tree[now]
    post(1)

    print(f'#{tc} {tree[l]}')