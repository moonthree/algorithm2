n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
cnt = 0
while k != 0:
    for i in coin:
        if k - i >= 0:
            k -= i
            cnt += 1
            break

print(cnt)