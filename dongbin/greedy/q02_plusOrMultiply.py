# 내 답안
# s = int(input())
#
# s_str = str(s)
# s_arr = []
# for i in s_str:
#     s_arr.append(int(i))
#
# result = 0
# for i in range(len(s_arr)):
#     if s_arr[i] == 0:
#         result = result + s_arr[i] + s_arr[i+1]
#     if i == 0 and s_arr[i] != 0:
#         result = 1 * s_arr[i]
#     else:
#         result = result * s_arr[i]
#
# print(result)


# 동빈나 ver
data = input()
result = int(data[0])       # 첫 번째 문자를 숫자로 변경하여 대입

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:     # 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기말고 더하기 수행
        result += num
    else:
        result *= num

print(result)