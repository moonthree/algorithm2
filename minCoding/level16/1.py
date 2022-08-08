
a = [list(map(str, input().split())) for _ in range(3)]

for i in range(3):
    print(a[i][0][-1], end='')