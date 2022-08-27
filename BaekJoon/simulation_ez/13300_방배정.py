import math

n, k = map(int, input().split())
arr = [[0] * 7 for _ in range(2)]  # 성별 / 학년별

for _ in range(n):
    gender, year = map(int, input().split())
    arr[gender][year] += 1

room = 0
for i in arr:
    for j in i:
        room += math.ceil(j / k)
print(room)
