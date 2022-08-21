# pattern 개수 구하기

pattern = [[1, 1], [1, 0]]

'''
5 4
1 1 1 1
1 0 1 1
1 1 1 1
1 1 0 1
1 0 1 1
'''

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def ispattern(dy, dx):
    for y in range(2):
        for x in range(2):
            if arr[dy+y][dx+x] != pattern[y][x]:
                return 0
    return 1

cnt = 0
for y in range(n-1):
    for x in range(m-1):
        cnt += ispattern(y, x)

print(cnt)