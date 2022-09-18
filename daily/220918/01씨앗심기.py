# 크기 : 7
# 씨앗위치 : 4, 1 // 2, 6

from collections import deque
n = int(input())
garden = [[0]*n for _ in range(n)]
flower = []
for _ in range(2):
    y, x = map(int, input().split())
    garden[y][x] = 1
    flower.append([y, x])

answer = 0
def bfs(flower, level):
    global q, answer
    q = deque(flower)
    #print(q)
    while q:
        nowy, nowx = q.popleft()
        print(q)
        garden[nowy][nowx] = level
        answer = level

        directy = [-1, 1, 0, 0]
        directx = [0, 0, -1, 1]
        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                continue
            if garden[dy][dx] != 0:
                continue
            garden[dy][dx] = garden[nowy][nowx] + 1
            q.append([dy, dx])

bfs(flower, 0)


print(answer)
