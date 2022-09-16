from collections import deque

name = list(input().split())  # A B C D
arr = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
]
used = [0] * 4
answer = []


def bfs(st):
    global answer
    q = deque()
    q.append(st)
    while q:
        now = q.popleft()
        answer.append(name[now])
        for i in range(4):
            if arr[now][i] == 1:
                if used[i] == 0:
                    used[i] = 1
                    q.append(i)


used[3] = 1  # 시작 index에 1체크
bfs(3)  # 시작 index 적고 시작
print(*answer)
