branch, level = map(int, input().split())

cnt = 0
def func(n):
    global cnt
    cnt += 1

    if n == level:
        return
    for _ in range(branch):
        func(n + 1)

func(0)
print(cnt)