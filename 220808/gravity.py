'''
9
7 4 2 0 0 6 0 7 0
1. 가장 큰 수 찾기, 내장함수 사용 금지
'''


N = int(input())
arr = list(map(int, input().split()))

#1
maxV = arr[0] # 첫 원소를 최대값으로 가정
for i in range(1, N): # 나머지 모든 원소에 대해
    if arr[i] > maxV:
        maxV = arr[i]
print(maxV)