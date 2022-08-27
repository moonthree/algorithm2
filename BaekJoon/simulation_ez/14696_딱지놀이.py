# 1. 별          4
# 2. 동그라미    3
# 3. 네모        2
# 4. 세모        1
# 다 같으면 무승부

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    a.pop(0)
    b.pop(0)
    a.sort()
    b.sort()
    flag = 1
    while len(a) > 0 and len(b) >0:
        a_pick = a.pop()
        b_pick = b.pop()
        if a_pick > b_pick:
            print('A')
            flag = 0
            break
        elif a_pick < b_pick:
            print('B')
            flag = 0
            break
        else:
            continue

    if flag:
        if len(a) > len(b):
            print('A')
        elif len(b) > len(a):
            print('B')
        elif len(a) == len(b):
            print('D')
