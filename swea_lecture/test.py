for tc in range(1, 11):
    dump_times = int(input())
    a = list(map(int, input().split()))

    for _ in range(dump_times):
        MAX = 0
        MIN = 101
        max_idx = 0
        min_idx = 0
        for i in range(len(a)):
            if a[i] > MAX:
                MAX = a[i]
                max_idx = i
            if a[i] < MIN:
                MIN = a[i]
                min_idx = i
        a[max_idx] -= 1
        a[min_idx] += 1

    print(f'#{tc} {max(a) - min(a)}')