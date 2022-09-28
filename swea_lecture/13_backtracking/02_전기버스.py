def dfs(idx, cnt):
    global move
    if cnt >= move:
        return
    # 종점에 가거나 넘으면
    if idx >= stop-1:
        if cnt <= move:   # 작으면 갱신
            move = cnt
        return

    for i in range(arr[idx]):
        dfs(idx+1+i, cnt+1)

t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    stop = arr.pop(0)
    move = int(21e8)
    dfs(0, 0)

    print(f'#{tc} {move-1}')