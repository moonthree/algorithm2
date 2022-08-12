arr = [['_', '_', '_'],
       ['_', '_', '_'],
       ['A', 'T', 'K'],
       ['_', '_', '_'],
       ['_', '_', '_']
       ]

arr2 = [['_']*3 for _ in range(5)]

ay, ax = 2, 0
ty, tx = 2, 1
ky, kx = 2, 2

for _ in range(7):
    a, b = input().split()

    if a == 'A':
        if b == 'UP':
            ay -= 1
        elif b == 'DOWN':
            ay += 1
        elif b == 'RIGHT':
            ax += 1
        elif b == 'LEFT':
            ax -= 1

    if a == 'T':
        if b == 'UP':
            ty -= 1
        elif b == 'DOWN':
            ty += 1
        elif b == 'RIGHT':
            tx += 1
        elif b == 'LEFT':
            tx -= 1

    if a == 'K':
        if b == 'UP':
            ky -= 1
        elif b == 'DOWN':
            ky += 1
        elif b == 'RIGHT':
            kx += 1
        elif b == 'LEFT':
            kx -= 1

arr2[ay][ax] = 'A'
arr2[ty][tx] = 'T'
arr2[ky][kx] = 'K'

for y in range(len(arr2)):
    for x in range(len(arr2[y])):
        print(arr2[y][x], end='')
    print()
