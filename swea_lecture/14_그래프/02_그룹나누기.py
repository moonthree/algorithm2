def findboss(member):
    global bucket
    if bucket[member] == 0:
        return member
    ret = findboss(bucket[member])
    return ret

def union(a, b):
    global bucket
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return
    bucket[bboss] = aboss


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bucket = [0]*(n+1)
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])

    cnt = 0
    for i in range(1, len(bucket)):
        if bucket[i] == 0:
            cnt += 1
    print(f'#{tc} {cnt}')

# 3
# 5 2
# 1 2 3 4
# 5 3
# 1 2 2 3 4 5
# 7 4
# 2 3 4 5 4 6 7 4