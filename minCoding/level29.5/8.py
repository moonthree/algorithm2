arr_map = [list(input()) for _ in range(4)]
direct_y = [0, 1, 0, -1]
direct_x = [1, 0, -1, 0]

arr = []
for y in range(len(arr_map)):
    for x in range(len(arr_map[y])):
        if arr_map[y][x].isupper():
            arr.append(arr_map[y][x])
arr.sort()

def move(sec, word):
    global arr_map
    for m in range(len(arr_map)):
        for n in range(len(arr_map[m])):
            if arr_map[m][n] == word:
                dy = m + direct_y[sec]
                dx = n + direct_x[sec]
                if dy < 0 or dx < 0 or dy > 3 or dx > 2 or arr_map[dy][dx] == '#' or arr_map[dy][dx].isupper() == True :
                    continue
                arr_map[dy][dx] = arr_map[m][n]
                arr_map[m][n] = '_'
for i in range(5):
    if i > 3:
        i = i % 4
    for j in arr:
        move(i, j)

for y in range(len(arr_map)):
    for x in range(len(arr_map[y])):
        print(arr_map[y][x], end='')
    print()