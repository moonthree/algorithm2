arr = [3, 7, 1, 5]
lv = 3
branch = 4

# 매개변수
def card(level, sum_card):

    if level == lv:
        print(sum_card, end=' ')
        return
    for i in range(branch):
        card(level+1, sum_card+arr[i])

card(0, 0)


print()
# 전역변수
sum_global = 0

def g_card(level):
    global sum_global
    if level == lv:
        print(sum_global, end=' ')
        return
    for i in range(branch):
        sum_global += arr[i]
        g_card(level+1)
        sum_global -= arr[i]

g_card(0)