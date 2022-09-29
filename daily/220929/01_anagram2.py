a = input()
b = input()

bucket_a = [0]*200
bucket_b = [0]*200

for i in a:
    bucket_a[ord(i)] += 1
for i in b:
    bucket_b[ord(i)] += 1

cnt = 0
for i in range(200):
    if bucket_a[i] != bucket_b[i]:
        cnt += abs(bucket_a[i] - bucket_b[i])
print(cnt)
