for t in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    while True:
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))
        arr[max_idx] -= 1
        arr[min_idx] += 1
        dump -= 1
        if dump == 0:
            break

    print(f'#{t} {max(arr) - min(arr)}')