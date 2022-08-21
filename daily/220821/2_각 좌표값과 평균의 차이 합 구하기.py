# n 입력
# n*n 배열을 입력
# 배열 전체 평균 구하고
# 각 좌표값과 배열평균의 차이의 합 구하기

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ssum = 0
for i in range(n):
    for j in range(n):
        ssum += arr[i][j]
avg = ssum/(n*n)
print('평균 : ', int(avg))

sum_avg = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > avg:
            sum_avg += arr[i][j] - avg
        else:
            sum_avg += avg - arr[i][j]
print(int(sum_avg))
'''
5
2 4 7 4 2
2 9 5 3 1
4 9 6 5 3
3 7 9 2 3
1 1 2 3 4
'''