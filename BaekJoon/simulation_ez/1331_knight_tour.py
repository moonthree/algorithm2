visited = [[0]*6 for _ in range(6)]

dy = ['6', '5', '4', '3', '2', '1']
dx = ['A', 'B', 'C', 'D', 'E', 'F']

flag = 0

for _ in range(36):
    input_x, input_y = map(str, input())
    visited[dy.index(input_y)][dx.index(input_x)] += 1

    if visited[dy.index(input_y)][dx.index(input_x)] > 1:
        flag = 1
        break

for y in range(6):
    for x in range(6):
        print(visited[y][x], end=' ')
    print()

if flag:
    print('Invalid')
else:
    print('Valid')