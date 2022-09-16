n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
i = 0
for j in range(1, n - 2):
    arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
arr[i][0], arr[i][n - 1] = arr[i][n - 1], arr[i][0]

print(*arr)