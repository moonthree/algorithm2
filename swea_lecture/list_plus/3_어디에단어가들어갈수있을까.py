def wow(yy, xx):
    global cnt
    i = 0
    cnt_garo = 0
    while True:
        dy = yy
        dx = xx + i
        if dx > n-1 or arr[dy][dx] == 0:
            break
        i += 1
        cnt_garo += 1
    if cnt_garo == word:
        cnt += 1
def wow_sero(yy, xx):
    global cnt
    i = 0
    cnt_sero = 0
    while True:
        dy = yy + i
        dx = xx
        if dy > n - 1 or arr[dy][dx] == 0:
            break
        i += 1
        cnt_sero += 1
    if cnt_sero == word:
        cnt += 1

t = int(input())

for tc in range(1, t+1):
    n, word = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for y in range(len(arr)):
        for x in range(len(arr)):
            if arr[y][x] == 1:
                if y-1 < 0 or arr[y-1][x] == 0:
                    wow_sero(y, x)
                if x-1 < 0 or arr[y][x-1] == 0:
                    wow(y, x)

    print(f'#{tc} {cnt}')

