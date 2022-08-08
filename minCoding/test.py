# a = int(input())
# print(a)

# 3 6
# a, b = map(int, input().split())
# print(a, b)

# num_list = list(map(int, input().split()))
# print(num_list)

# n = int(input())
# b = [input() for _ in range(n)]
# for i in b:
#     print(i)
#
# n, m = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(n)]

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
for j in range(len(a)):
    for i in range(len(b)):
        print(a[i])