arr = [9, 7, 1, 8, 5]
# 매개변수
def abc(level, sums):
    if level == 4:
        print(sums, end=' ')
        return
    print(sums, end=' ')
    abc(level + 1, sums + arr[level + 1])
    print(sums, end=' ')

abc(0, arr[0])

print()
# 전역변수
g_sum = arr[0]
def abcd(level):
    global g_sum
    print(g_sum, end=' ')
    if level == 4:
        return

    g_sum += arr[level+1]
    abcd(level+1)
    g_sum -= arr[level+1]
    print(g_sum, end=' ')

abcd(0)