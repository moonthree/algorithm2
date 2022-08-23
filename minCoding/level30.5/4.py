arr = [input() for _ in range(3)]
len_arr = []
for i in range(len(arr)):
    len_arr.append(len(arr[i]))
maxi = max(len_arr)

max_arr = []
for i in range(len(arr)):
    if maxi == len(arr[i]):
        max_arr.append(arr[i])

if len(max_arr) == 1:
    print(max_arr[0])
elif len(max_arr) == 2:
    for i in range(maxi):
        if max_arr[0][i] != max_arr[1][i]:
            if max_arr[0][i] == '0':
                print(max_arr[1])
                break
else:
    temp = []
    for i in range(maxi):
        if max_arr[0][i] != max_arr[1][i]:
            if max_arr[0][i] == '0':
                temp.append(max_arr[1])
                break
            else:
                temp.append(max_arr[0])
                break
    for i in range(maxi):
        if temp[0][i] != max_arr[2][i]:
            if temp[0][i] == '0':
                print(max_arr[2])
                break
            else:
                print(temp[0])
                break





# def big(word1, word2):
#
#
# maxi = int(-21e8)
# maxi_2 = []
# maxi_same = []
# for i in range(len(arr)):
#     if len(arr[i]) > maxi:
#         maxi = len(arr[i])
#         maxi_2 = arr[i]
#     if len(maxi_2) == len(arr[i]):
#         maxi_same = arr[i]
#
# if len(maxi_2) == len(maxi_same):
#     print(big(maxi_2, maxi_same))
# else:
#     print(maxi_2)