arr = [5, 9, 7, 3, 1, 5, 6, 4]


# 매개변수
def abc(level, sums):
    if level == len(arr) - 1:
        print(sums, end=' ')
        return
    print(sums, end=' ')
    abc(level + 1, sums + arr[level + 1])
    print(sums, end=' ')


abc(0, arr[0])

print()

# 전역변수
sum_global = 5


def abcd(level):
    global sum_global
    if level == len(arr) - 1:
        print(sum_global, end=' ')
        return
    print(sum_global, end=' ')
    sum_global += arr[level + 1]

    abcd(level + 1)

    sum_global -= arr[level + 1]
    print(sum_global, end=' ')


abcd(0)
