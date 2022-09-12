arr = [list(input()) for _ in range(4)]

# asdqwd
for i in range(3, -1 , -1):
    for j in range(2, -1, -1):
        if arr[i][j] != '_':
            cnt = 0
            for k in range(3, i, -1):
                while arr[k-cnt][j] != '_':
                    cnt += 1
                arr[k-cnt][j]= arr[i][j]
                arr[i][j]= '_'
                break



for s in range(4):
    for t in range(3):
        print(arr[s][t], end='')
    print()