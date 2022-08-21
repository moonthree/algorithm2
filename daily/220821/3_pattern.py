'''
5 4
1 1 1 1
1 0 1 1
1 1 1 1
1 1 0 1
1 0 1 1
'''
# pattern 찾기
# n = 세로 m = 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pattern = [[1, 1], [1, 0]]

# 00 01
# 10 11

def ispattern(dy, dx):
    direct_y = [0, 0, 1, 1]
    direct_x = [0, 1, 0, 1]
    for i in range(2):
        for j in range(2):
            if pattern[i][j] != arr[dy+i][dx+j]:
                return 0
    return 1
ret = 0
for i in range(n-1):
    for j in range(m-1):
        ret += ispattern(i, j)

print(ret)