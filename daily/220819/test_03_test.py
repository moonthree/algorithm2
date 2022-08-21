n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# 2 4 7 4 2
# 2 9 5 3 1
# 4 9 6 5 3
# 3 7 9 2 3
# 1 1 2 3 4

# 1. 배열 전체 평균 구하기
# 2. 각 좌표값이 배열평균과 차이는 값들의 합 출력하긴

sums = 0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        sums += arr[y][x]

avg = int(sums/n**2)
print('평균 : ', avg)

sums2 = 0
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] - avg > 0:
            sums2 += arr[y][x] - avg
        else:
            sums2 -= arr[y][x] - avg
print('총합 : ', sums2)