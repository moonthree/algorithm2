input_arr = [list(map(int, input().split())) for _ in range(4)]

vect = [[0 for _ in range(3)] for _ in range(4)]


def change(y, x):
    vect[y][x] = 5

for i in range(len(input_arr)):
    for _ in range(len(input_arr[i])):
        if input_arr[i][0] < 0 or input_arr[i][0] > 3 or input_arr[i][1] < 0 or input_arr[i][1] > 2:
            continue
        change(input_arr[i][0], input_arr[i][1])

for i in range(len(vect)):
    for j in range(len(vect[i])):
        print(vect[i][j], end=' ')
    print()