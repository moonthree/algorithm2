<<<<<<< HEAD
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    directy1 = [-1, 1, 0, 0]
    directx1 = [0, 0, -1, 1]
    directy2 = [-1, 1, -1, 1]
    directx2 = [1, 1, -1, -1]


    def rowcol(y, x):
        sum1 = arr[y][x]
        for a in range(4):
            for i in range(1, M):
                ny1 = y + directy1[a]*(i)
                nx1 = x + directx1[a]*(i)

                if ny1<0 or nx1<0 or ny1>N-1 or nx1> N-1: continue

                sum1 += arr[ny1][nx1]

        return sum1

    def diag(y, x):
        sum2 = arr[y][x]
        for b in range(4):
            for j in range(1, M):
                ny2 = y + directy2[b]*(j)
                nx2 = x + directx2[b]*(j)

                if ny2 < 0 or nx2 < 0 or ny2 > N - 1 or nx2 > N - 1: continue

                sum2 += arr[ny2][nx2]

        return sum2

    MAX1 = 0
    MAX2 = 0
    for s in range(N):
        for t in range(N):
            if rowcol(s, t)> MAX1:
                MAX1 = rowcol(s, t)
            if diag(s, t)> MAX2:
                MAX2 = diag(s, t)
    print(MAX1)
    print(MAX2)

    if MAX1>MAX2:
        print(f'#{tc} {MAX1}')
    elif MAX2>=MAX1:
        print(f'#{tc} {MAX2}')
=======
for tc in range(1, 11):
    dump_times = int(input())
    a = list(map(int, input().split()))

    for _ in range(dump_times):
        MAX = 0
        MIN = 101
        max_idx = 0
        min_idx = 0
        for i in range(len(a)):
            if a[i] > MAX:
                MAX = a[i]
                max_idx = i
            if a[i] < MIN:
                MIN = a[i]
                min_idx = i
        a[max_idx] -= 1
        a[min_idx] += 1

    print(f'#{tc} {max(a) - min(a)}')
>>>>>>> 5facc8216f978433b252a4837f3d8b6be65730ac
