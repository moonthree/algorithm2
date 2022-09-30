n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

INF = int(21e8)
for i in range(n):
    for j in range(n):
        if i != j and arr[i][j] == 0:
            arr[i][j] = INF



for k in range(n):
    for s in range(n):
        for d in range(n):
            if arr[s][d] > arr[s][k] + arr[k][d]:
                arr[s][d] = arr[s][k] + arr[k][d]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
