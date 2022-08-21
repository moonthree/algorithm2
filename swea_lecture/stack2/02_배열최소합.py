t = int(input())

def abc(y, ssum):
    global mini
    if ssum > mini:
        return
    if y == n :
        if ssum < mini:
            mini = ssum
        return

    for x in range(n):
        if used[x] == 1:
            continue
        used[x] = 1
        abc(y+1, ssum+arr[y][x])
        used[x] = 0


for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mini = int(21e8)
    used = [0]*n
    abc(0, 0)
    print(f'#{tc} {mini}')