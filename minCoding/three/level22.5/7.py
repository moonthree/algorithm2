arr = [
    [
        [0, 1, 0],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
]

n = int(input())

for i in range(len(arr[n])):
    for j in range(len(arr[n][i])):
        if arr[n][i][j] == 0:
            print(' ', end='')
        else:
            print('#', end='')
    print()