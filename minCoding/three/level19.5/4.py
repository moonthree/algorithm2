arr = [[0 for _ in range(4)]for _ in range(4)]

color = [input().split() for _ in range(3)]

def draw(a, b):
    if a == 'G':
        for i in range(4):
            arr[int(b)][i] = 1
    if a == 'S':
        for i in range(4):
            arr[i][int(b)] = 1

for i in range(len(color)):
    draw(color[i][0], color[i][1])

for y in range(len(arr)):
    for x in range(len(arr[y])):
        print(arr[y][x], end=' ')
    print()
