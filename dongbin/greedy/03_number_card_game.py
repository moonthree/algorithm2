# 숫자카드게임

n, m = map(int, input().split())

result = 0

# n,m의 이차원 배열이지만 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))          # 1행씩 입력
    min_value = min(data)                           # 현재 줄에서 가장 작은 수 찾기
    result = max(result, min_value)                 # result, min_value 중 비교하여 큰 수 저장

print(result)