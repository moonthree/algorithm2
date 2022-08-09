vect = ['B', 'T', 'K', 'I', 'G', 'Z']

target = list(map(str, input().split()))

cnt = 0
for i in target:
    for j in vect:
        if i == j:
            cnt += 1
print(cnt)