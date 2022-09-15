cnt = 0


def abc(level, sum):
    global n, cnt
    if level == n:
        if sum == 10:
            cnt += 1
        return
    for i in range(1, 5):
        abc(level + 1, sum + i)


n = int(input())
abc(0, 0)  # level sum
print(cnt)
