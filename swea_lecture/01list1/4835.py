test_case = int(input())

for t in range(1, test_case+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    MAX = int(-21e8)
    MIN = int(21e8)
    for i in range(len(nums) - M + 1):
        sums = 0
        for j in range(i, M+i):
            sums += nums[j]
        if sums > MAX:
            MAX = sums
        if sums < MIN:
            MIN = sums

    print(f'#{t} {MAX-MIN}')