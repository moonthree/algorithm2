# 동빈나 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
print(target)

# 내 답안
# n = int(input())
# arr = list(map(int, input().split()))
#
# arr.sort()
#
# make_money = []
# for i in range(len(arr)):
#     make_money.append(arr[i])
#     ret = 0
#     for j in range(i, len(arr)):
#         ret += arr[j]
#         make_money.append(ret)
#
# num = 1
# while True:
#     cnt = 0
#     for i in make_money:
#         if i == num:
#             cnt += 1
#             break
#     if cnt == 0:
#         break
#     else:
#         num += 1
#
# print(num)