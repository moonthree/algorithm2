n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


boss = 0
for y in range(n):
    if arr[y][0] == 1:
        boss = y
        print(f'boss:{y}')

under = []
for x in range(n):
    if arr[0][x] == 1:
        under.append(x)

print('under:', end='')
for i in under:
    print(i, end=' ')