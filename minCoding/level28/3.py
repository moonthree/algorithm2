name = ['A', 'B', 'H', 'C', 'D', 'F', 'G', 'E']
arr = [[0, 1, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 1],
       [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]
       ]
word = input()
idx = -1
for i in range(len(name)):
    if word == name[i]:
        idx = i

boss = -1
for y in range(len(arr)):
    if arr[y][idx] == 1:
        boss = y
# boss 검색

bro = []
for i in range(len(arr)):
    if arr[boss][i] == 1:
        bro.append(i)

if len(bro) > 1:
    for i in bro:
        if i == idx:
            continue
        else:
            print(name[i], end=' ')
else:
    print('없음')