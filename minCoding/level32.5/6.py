n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

arr_new = [[0]*n for _ in range(n)]

spin_turn = k % 4
if spin_turn == 1:
    for i in range(n):
        for j in range(n):
            arr_new[i][j] = arr[n-1-j][i]
elif spin_turn == 2:
    for i in range(n):
        for j in range(n):
            arr_new[i][j] = arr[n-1-i][n-1-j]
elif spin_turn == 3:
    for i in range(n):
        for j in range(n):
            arr_new[i][j] = arr[j][i]

for y in range(n):
    for x in range(n):
        print(arr_new[y][x], end=' ')
    print()