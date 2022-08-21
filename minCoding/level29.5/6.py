arr = [[3, 2, 5, 3],
       [7, 6, 1, 6],
       [4, 9, 2, 7]
       ]
# 1 2 3
# 2 1 3
# 3 1 2

num_arr = list(map(int, input().split()))


def gear(x, num):
    global arr
    for _ in range(num):
        arr[0][x], arr[1][x] = arr[1][x], arr[0][x]
        arr[0][x], arr[2][x] = arr[2][x], arr[0][x]


for i in range(len(num_arr)):
    gear(i, num_arr[i])

for y in range(len(arr)):
    for x in range(len(arr[y])):
        print(arr[y][x], end='')
    print()
