n = int(input())
a = list(map(int, input().split()))

bucket = [0]*101
# dat 등록
for i in range(n):
    bucket[a[i]] += 1

# 누적합 구하기
for i in range(1, len(bucket)):
    bucket[i] += bucket[i-1]   # bucket[i] = bucket[i] + bucket[i-1]

# 값넣기
result = [0]*101
for i in range(n):
    index = a[i]
    result[bucket[index]-1] = a[i]
    bucket[index] -= 1