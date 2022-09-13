t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxi = int(-21e8)

    def fly(y, x):
        global maxi
        ssum = 0
        for i in range(m):
            for j in range(m):
                dy = i+y
                dx = j+x
                if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                    continue
                ssum += arr[dy][dx]
        if ssum > maxi:
            maxi = ssum

    for y in range(n):
        for x in range(n):
            fly(y, x)
    print(f'#{tc} {maxi}')