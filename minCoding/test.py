# arr = [['A', 7, 9, 'T', 'K', 'Q'], ['M', 'I', 'N', 'C', 'O', 'D']]
#
# letter = input().split()
#
# for i in arr:
#     for j in i:
#         for x in letter:
#             if j in letter:
#                 print(f'{x} : 존재')
#             else:
#                 print(f'{x} : 없음')

rule = input().split()

rule[0] = int(rule[0])
rule[1] = int(rule[1])

# # rule[0] = 열
# # rule[1] = 행
# # rule[2] = 값

arr = [rule[2]*rule[1] for i in range(rule[0])]

for i in arr:
    print(i)