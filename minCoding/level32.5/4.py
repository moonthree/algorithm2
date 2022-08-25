n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

down = []
up = []

for i in arr:
    if i[1] == 'DOWN':
        down.append(int(i[0]))
    else:
        up.append(int(i[0]))

big = 50
small = 0
if down:
    big = min(down)
if up:
    small = max(up)

if big <= small:
    print('ERROR')
elif big-small == 2:
    print(big-1)
else:
    print(f'{small+1} ~ {big-1}')
