A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
for i in range(len(A)):
    result.append(A[i]+B[len(B)-i-1])

for i in result:
    print(i, end=' ')