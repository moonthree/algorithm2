vect = list(map(int, input().split()))
bucket = [0]*(len(vect)+10)

for i in range(len(vect)):
    bucket[vect[i]] += 1

for i in range(len(bucket)):
    for j in range(bucket[i]):
        print(i, end=' ')
