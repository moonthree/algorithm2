arr = [[0 for _ in range(6)] for _ in range(3)]

uni = 65
for x in range(2, -1, -1):
    for y in range(5, -1, -1):
        arr[x][y] = chr(uni)
        uni += 1

x, y = map(int, input().split())
print(arr[y][x])