n, m = map(int, input().split())

arr = [list(map(str, input().split())) for _ in range(m)]

bucket = [0]*n

for i in arr:
    bucket[int(i[0])] += 1

max_vote = max(bucket)
elected = 0
for i in range(n):
    if bucket[i] == max_vote:
        elected = i
        break

for i in arr:
    if i[0] == str(elected):
        print(i[1], end=' ')