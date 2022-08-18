name = ['Amy', 'Bob', 'Chloe', 'Edger', 'Diane']
# 0, 1, 2, 3, 4

arr = [[0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0]
       ]

like = [0]*5

for x in range(5):
    for y in range(5):
        if arr[y][x] == 1:
            like[x] += 1

likely = max(like)
likely_idx = like.index(likely)

print(name[likely_idx])