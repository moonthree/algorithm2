def getWinner(p1, p2, arr):
    temp = arr[p1] - arr[p2]
    if temp == -1 or temp == 2:
        return p2
    return p1


def recur(st, end, arr):
    if st >= end:
        return st
    mid = (st + end) // 2
    p1 = recur(st, mid, arr)
    p2 = recur(mid + 1, end, arr)
    return getWinner(p1, p2, arr)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    winner = recur(0, len(arr) - 1, arr)
    print(f'#{t} {winner + 1}')
