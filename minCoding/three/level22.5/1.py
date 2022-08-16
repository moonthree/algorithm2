# 3차 배열 pass가 아니었네


arr = [[
    ['A', 'T', 'B'],
    ['C', 'C', 'B']
],
    [['A', 'A', 'A'],
     ['B', 'B', 'C']
     ]
]

n = input()
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            if arr[i][j][k] == n:
                cnt += 1

if cnt:
    print('발견')
else:
    print('미발견')