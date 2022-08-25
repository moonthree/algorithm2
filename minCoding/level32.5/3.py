def reverse(y, x):
    for i in range(5):
        dy = y + directy[i]
        dx = x + directx[i]

        if dy < 0 or dx < 0 or dy > 2 or dx > 5:
            continue
        if arr2[dy][dx] == '#':
            arr2[dy][dx] = arr[dy][dx]
        else:
            arr2[dy][dx] = '#'

arr = [['A', 'B', 'C', 'E', 'F', 'G'],
       ['H', 'I', 'J', 'K', 'L', 'M'],
       ['N', 'O', 'P', 'Q', 'R', 'S']
       ]
arr2 = [['A', 'B', 'C', 'E', 'F', 'G'],
       ['H', 'I', 'J', 'K', 'L', 'M'],
       ['N', 'O', 'P', 'Q', 'R', 'S']
       ]

directy = [-1, 1, 0, 0, 0]
directx = [0, 0, -1, 1, 0]

words = input()

for k in range(len(words)):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == words[k]:
                reverse(i, j)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr2[i][j], end='')
    print()