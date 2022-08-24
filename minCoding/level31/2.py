# 슬라이딩 윈도우
def sliding_window(arr, k):
    min_sum = int(21e8)
    window_sum = 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]

        if end >= k - 1:
            if window_sum <= min_sum:
                min_sum = window_sum
            window_sum -= arr[start]
            start += 1
    return min_sum

n = int(input())
arr = list(map(int, input().split()))

print(sliding_window(arr, 4))