T = int(input())
for t in range(1, T + 1):
    N = int(input()) // 10
    dp = [0] * (N + 1)
    dp[1] = 1
    if N > 1:
        dp[2] = 3
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2
    print(f"#{t} {dp[N]}")