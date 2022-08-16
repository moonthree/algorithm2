arr = [4, -7, 1, 3]
lv = 4
branch = 4

cnt = 0
#매개변수
def card(level, sums):
    global cnt
    if level == lv:
        if sums > 10:
            cnt += 1
        return

    for i in range(branch):
        card(level+1, sums+arr[i])

card(0, 0)
print(cnt)

print()
g_cnt = 0
g_sums = 0
def g_card(level):
    global g_cnt
    global g_sums
    if level == lv:
        if g_sums > 10:
            g_cnt += 1
        return
    for i in range(branch):
        g_sums += arr[i]
        g_card(level+1)
        g_sums -= arr[i]
g_card(0)
print(g_cnt)