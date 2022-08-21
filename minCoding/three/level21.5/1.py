arr = [list(input()) for _ in range(4)]

ay, ax = 0, 0
by, bx = 0, 0

for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == 'A':
            ay, ax = y, x
        elif arr[y][x] == 'B':
            by, bx = y, x

distance = abs(ay-by) + abs(ax-bx)
print(distance)

