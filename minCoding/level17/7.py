mask = [[0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]
arr = [[3, 5, 4, 1, 1], [3, 5, 2, 5, 6]]

num = int(input())

a = False
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 1:
            if num == arr[i][j]:
                a = True

if a:
    print(f'{num} 존재')
else:
    print(f'{num} 없음')