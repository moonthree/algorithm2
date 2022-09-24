# 1~6학년
# 동일 성별끼리
import math
n, k = map(int, input().split())

room = [[0]*7 for _ in range(2)]

for _ in range(n):
    s, y = map(int, input().split())
    room[s][y] += 1

cnt = 0

for y in range(2):
    for x in range(7):
        cnt += math.ceil(room[y][x]/k)

print(cnt)