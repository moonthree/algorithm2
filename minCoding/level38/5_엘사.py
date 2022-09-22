from collections import deque

def bfs(sty1, stx1, sty2, stx2):
    q = deque()
    q.append([sty1, stx1, 0])

    q2 = deque()
    q2.append([sty2, stx2])
    Map = [[0]*n for _ in range(n)]
    Map2 = [[0] * n for _ in range(n)]
    visited1 = [[False]*n for _ in range(n)]
    visited2 = [[False]*n for _ in range(n)]
    visited1[sty1][stx1] = True
    visited2[sty2][stx2] = True

    directy1 = [-1, 1, 0, 0, 1, -1, 1, -1]
    directx1 = [0, 0, -1, 1, 1, -1, -1, 1]
    directy2 = [-1, 1, 0, 0, 0]
    directx2 = [0, 0, -1, 1, 0]
    directy3 = [-1, 1, 0, 0]
    directx3 = [0, 0, -1, 1]

    while q:
        now = q.popleft()
        nowy1, nowx1, level = now[0], now[1], now[2]
        if nowx1 == stx2 and nowy1 == sty2:
            if level % 2 == 0:
                print(f'{level//2} sec')
            else:
                print(f'{level // 2 + 1} sec')
        # now2 = q2.popleft()
        # nowy2, nowx2 = now2[0], now2[1]
        #print(nowy1, nowx1, ' : ', nowy2, nowx2)
        # if nowy1 == nowy2 and nowx1 == nowx2:
        #     answer.append(level)

        inside = 0
        # if abs(nowx1-stx2) + abs(nowy1-sty2) <= 4:
        #     inside = 1
        if inside:
            for i in range(4):
                dy = directy3[i] + nowy1
                dx = directx3[i] + nowx1
                if dy < 0 or dx < 0 or dy > n-1 or dx > n-1:
                    continue
                if visited1[dy][dx] or arr[dy][dx] == '#':
                    continue
                q.append([dy, dx, level+1])
                visited1[dy][dx] = True
                Map[dy][dx] = level+1
        else:
            for i in range(8):
                dy = directy1[i] + nowy1
                dx = directx1[i] + nowx1
                if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
                    continue
                if visited1[dy][dx] or arr[dy][dx] == '#':
                    continue
                q.append([dy, dx, level + 1])
                visited1[dy][dx] = True
                Map[dy][dx] = level + 1
        # for i in range(5):
        #     dy = directy2[i] + nowy2
        #     dx = directx2[i] + nowx2
        #     if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1:
        #         continue
        #     if visited2[dy][dx] or arr[dy][dx] == '#':
        #         continue
        #     q2.append([dy, dx])
        #     visited2[dy][dx] = True
        #     Map2[dy][dx] = -(level + 1)
    # for i in range(n):
    #     for j in range(n):
    #         print(Map[i][j], end=' ')
    #     print()
    # for i in range(n):
    #     for j in range(n):
    #         print(Map2[i][j], end=' ')
    #     print()
    # MIN = 21e8
    # for i in range(n):
    #     for j in range(n):
    #         if Map[i][j] == -(Map2[i][j]) and Map[i][j] != 0:
    #             MIN = min(Map[i][j], MIN)
    # print(f'{MIN} sec')


n = int(input())
arr = [list(input()) for _ in range(n)]
y1, x1, y2, x2 = map(int, input().split())
answer = []
bfs(y1, x1, y2, x2)
# print(f'{min(answer)} sec')
