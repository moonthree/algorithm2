arr = [[0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 1, 1, 0],
       [0, 0, 0, 0, 0], ]

flag = True
for y in range(4):
    for x in range(5):
        if arr[3 - y][4 - x] == 1:
            print(f'({3 - y},{4 - x})')
            flag = False
            break
    if flag == False:
        break
