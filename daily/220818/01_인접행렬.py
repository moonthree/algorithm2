# a b c d e

arr = [[0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1]
       ]

who = ['a', 'b', 'c', 'd', 'e']


popular = int(-21e8)
idx = 0
for x in range(len(arr)):
    cnt = 0
    for y in range(len(arr[x])):
        if arr[y][x] == 1:
            cnt += 1
    if cnt > popular:
        popular = cnt
        idx = x

print(who[idx])