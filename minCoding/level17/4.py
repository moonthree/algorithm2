arr = [['A', 'T', 'K', 'B'], ['C', 'Z', 'F', 'D'], ['H', 'G', 'E', 'I']]

a, input_y, input_x = input().split()

ay = 0
ax = 0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] == a:
            ay = y
            ax = x
            break

print(arr[ay+int(input_y)][ax+int(input_x)])