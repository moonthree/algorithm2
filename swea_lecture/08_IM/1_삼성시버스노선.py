t = int(input())

for tc in range(1, t+1):
    n = int(input())
    bucket = [0] * 5001
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            bucket[j] += 1

    p = int(input())
    bus_stop = []
    for i in range(p):
        bus_stop.append(int(input()))

    print(f'#{tc}', end=' ')
    for i in bus_stop:
        print(bucket[i], end=' ')
    print()


