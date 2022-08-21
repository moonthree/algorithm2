a, b = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(a)]

pattern = [[1, 1], [1, 0]]

# 00 01
# 10 11

def ispattern(y, x):
    cnt = 0
    for i in range(2):
        for j in range(2):
            dy = y+i
            dx = x+j
            # if dy < 0 or dx < 0 or dy > a-1 or dx > b-1:
            #     continue
            if arr[dy][dx] != pattern[i][j]:
                return 0
    return 1
    # if cnt == 4:
    #     return 1
    # else:
    #     return 0

num = 0
for y in range(a-1):
    for x in range(b-1):
        if ispattern(y, x):
            num += 1

print(num)