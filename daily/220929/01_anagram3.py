s1 = list(input())
s2 = list(input())

cnt = 0

for i in range(len(s2)-len(s1)+1):
    arr = s2[i:len(s1)+i]
    #print(arr)
    if sorted(s1) == sorted(arr):
        cnt += 1

print(cnt)







# bucket_s1 = [0]*200
#
# for i in s1:
#     bucket_s1[ord(i)] += 1
#
# cnt = 0
# for i in range(len(s2)):
#     bucket_s2 = [0] * 200
#     for j in range(i, len(s1)):
#         bucket_s2[ord(s2[j])] += 1
#     flag = 1
#     for k in range(200):
#         if bucket_s2[k] != bucket_s1[k]:
#             flag = 0
#     if flag:
#         cnt += 1
# print(cnt)