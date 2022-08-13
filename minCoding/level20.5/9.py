arr = [[3, 5, 4, 2, 5], [3, 3, 3, 2, 1], [3, 2, 6, 7, 8], [9, 1, 1, 3, 2]]

iy, ix = map(int, input().split())

def fluidPattern(y, x):
    Sum = 0
    for i in range(iy):
        for j in range(ix):
            dy = y + i
            dx = x + j

            if dy < 0 or dy > 3 or dx < 0 or dx > 4:
                continue
            Sum += arr[dy][dx]

    return Sum

MAX = int(-21e8)
y = 0
x = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if fluidPattern(i, j) > MAX:
            MAX = fluidPattern(i, j)
            y = i
            x = j

print(f'({y},{x})')