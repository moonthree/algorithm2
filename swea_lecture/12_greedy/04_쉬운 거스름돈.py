arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


t = int(input())
for tc in range(1, t+1):
    bucket = [0] * 8
    n = int(input())

    for i in range(len(arr)):
        if arr[i] <= n:
            a = n // arr[i]
            n = n % arr[i]
            bucket[i] += a
    print(f'#{tc}')
    print(*bucket)
