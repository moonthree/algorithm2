# MAX VALUE 출력하기
nums = [3, 6, 21, 4, 7]
# 1 max 내장함수 이용
print(max(nums))

# 2 sort
nums.sort()
print(nums[-1])

# 3 직접
MAX = int(-21e8)
for i in nums:
    if i > MAX:
        MAX = i
print(MAX)


# 리스트 안의 값들의 합 구하기
Sum = 0
for i in nums:
    Sum += i
print(Sum)

# 리스트 안에 최대값과 그 최대값의 등장 횟수 구하기
MAX2 = int(-21e8)
cnt = 0
for i in nums:
    if i > MAX2:
        MAX2 = i

for i in nums:
    if i == MAX2:
        cnt += 1
print(MAX2, cnt)