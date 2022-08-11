test_case = int(input())

for t in range(test_case):
    n = int(input())
    nums = list(map(int, input()))

    bucket = [0]*10

    for i in range(len(nums)):
        bucket[nums[i]] += 1

    MAX = int(-21e8)
    MAX_idx = 0
    for i in range(len(bucket)):
        if bucket[i] >= MAX:
            MAX = bucket[i]
            MAX_idx = i

    print(f'#{t+1} {MAX_idx} {MAX}')