t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    mini = int(21e8)
    maxi = int(-21e8)

    for i in range(n-m+1):
        ssum = 0
        for j in range(i, i+m):
            ssum += arr[j]

        if ssum > maxi:
            maxi = ssum
        if ssum < mini:
            mini = ssum

    print(maxi - mini)
