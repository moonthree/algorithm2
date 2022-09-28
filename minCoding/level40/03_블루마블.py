arr = list(map(int, input().split()))
dp = [0]*25

dp[2] = arr[2]
dp[3] = arr[3]

for i in range(4, len(arr)):
    if i % 2 == 0:
        temp = [dp[i-2], dp[i-3], dp[i//2]]
        dp[i] = max(temp) + arr[i]
    else:
        temp = [dp[i - 2], dp[i - 3]]
        dp[i] = max(temp) + arr[i]

print(max(dp))
