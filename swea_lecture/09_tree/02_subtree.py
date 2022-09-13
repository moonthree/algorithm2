def post(now):
    global cnt
    if now:
        post(left_son[now])
        post(right_son[now])
        cnt += 1

t = int(input())

for tc in range(1, t + 1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    v = e + 1
    left_son = [0] * (v + 1)
    right_son = [0] * (v + 1)
    cnt = 0

    for i in range(e):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left_son[p] == 0:
            left_son[p] = c
        else:
            right_son[p] = c

    post(n)
    print(f'#{tc} {cnt}')
