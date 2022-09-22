from collections import deque

def bfs(st):
    global cnt
    q = deque()
    q.append([st, 0])
    arr = [0]*100001
    arr[st] = 1

    while q:
        now = q.popleft()
        now_new, level = now[0], now[1]
        if now_new == d:
            print(level)
            break
        for i in range(4):
            if i == 0:
                next = int(now_new/2)
            elif i == 1:
                next = now_new*2
            elif i == 2:
                next = now_new + 1
            elif i == 3:
                next = now_new - 1

            if next < 0 or next > 100000 or arr[next] == 1:
                continue
            arr[next] = 1
            q.append([next, level + 1])


s = int(input())
d = int(input())
bfs(s)