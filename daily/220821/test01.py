# n 입력
# n*n 배열을 입력

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 배열 전체 평균 구하기
ssum = 0
for y in range(n):
    for x in range(n):
        ssum += arr[y][x]

avg = int(ssum/(n*n))
print(avg)

# 2. 각 좌표값이 배열평균과 차이는 값들의 합 출력하기
avg_sum = 0
for y in range(n):
    for x in range(n):
        if avg > arr[y][x]:
            avg_sum += avg - arr[y][x]
        else:
            avg_sum += arr[y][x] - avg
print(avg_sum)

'''
5
2 4 7 4 2
2 9 5 3 1
4 9 6 5 3
3 7 9 2 3
1 1 2 3 4
'''