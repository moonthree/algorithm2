t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr1 = [[0] * n for _ in range(n)]

    for i in range(1, n):
        arr1[0][i] = arr1[0][i - 1] + arr[0][i]
        arr1[i][0] = arr1[i - 1][0] + arr[i][0]

    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            arr1[i][j] = min(arr1[i - 1][j], arr1[i][j - 1]) + arr[i][j]

    print(f'#{tc} {arr1[n-1][n-1] + arr[0][0]}')