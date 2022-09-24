arr = [500, 100, 50, 10]
n = int(input())
cnt = 0

for i in arr:
    if n >= i:
        cnt += n // i
        n = n % i

print(cnt)