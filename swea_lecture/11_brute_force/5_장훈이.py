t = int(input())

def dfs(level, height, start):
    global MIN
    if height >= m:
        MIN = min(MIN, height-m)
        return
    # if level == n:
    #     return
    for i in range(start, n):
        dfs(level+1, height+arr[i], i+1)

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    used = [False]*n
    MIN = 21e8
    dfs(0, 0, 0)
    print(f'#{tc} {MIN}')
