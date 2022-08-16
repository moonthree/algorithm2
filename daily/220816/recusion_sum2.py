arr = [3, 4, 5, 1, 6, 9]

# 매개변수
def abc(level, sums):
    if level == 5:
        print(sums, end=' ')
        return
    abc(level + 1, sums + arr[level + 1])
    print(sums, end=' ')


abc(0, 3)


# sum_global = 3
#
#
# def abc_global(level):
#     global sum_global
#     if level == 5:
#         print(sum_global)
#         return
#     sum_global += arr[level + 1]
#     abc_global(level + 1)
#     sum_global -= arr[level - 1]
#     print(sum_global)
#
#
# abc_global(0)
