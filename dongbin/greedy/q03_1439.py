# 동빈나
data = input()
count0 = 0      # 전부 0으로 바꾸는 경우
count1 = 0      # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

# 내 풀이

# data = input()
# data2 = data
# cnt = 0
#
# zero = data.count('0')
# one = data.count('1')
#
# big = '0'
# small = '1'
# if one > zero:
#     big = '1'
#     small = '0'
#
#
# start = 0
# end = 0
# cnt = 0
# cnt2 = 0
# for i in range(len(data)):
#     if data[i] == small:
#         start = i
#         for j in range(i+1, len(data)):
#             if data[j] != small:
#                 end = j
#                 break
#         data = data.replace(small, big, end-start)
#         start = 0
#         end = 0
#         cnt += 1
#
# for i in range(len(data)):
#     if data2[i] == big:
#         start = i
#         for j in range(i+1, len(data2)):
#             if data2[j] != big:
#                 end = j
#                 break
#         data2 = data2.replace(big, small, end-start)
#         start = 0
#         end = 0
#         cnt2 += 1
#
# print(min(cnt, cnt2))