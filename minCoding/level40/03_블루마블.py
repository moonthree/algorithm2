arr = list(map(int, input().split()))
dp = [int(-21e8)]*25


for i in range(len(arr)):
    if i == 0:
        dp[i+2] = dp[i] + arr[i+2]



