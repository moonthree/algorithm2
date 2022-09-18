# 크기 : 7
# 씨앗위치 : 4, 1 // 2, 6

from collections import deque
n = int(input())
garden = [[0]*n for _ in range(n)]
q = deque()
for _ in range(2):
    y, x = map(int, input().split())
    garden[y][x] = 1
    q.append([y, x])

def bfs(flower):
    global q
    while q:
        nowy, nowx = q.popleft()
        garden[nowy][nowx] = level



bfs(q)



