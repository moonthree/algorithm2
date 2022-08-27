# n명의 손님
# m초의 시간을 들이면 k 개의 붕어빵 생성
# n명의 손님이 오는 시간이 있는 리스트

t = int(input())

for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))

    flag = 0
    sec = 0
    cnt = 0
    c_sec = 0
    while c_sec < max(customer) + 1:
        sec += 1
        c_sec += 1
        if m == sec:
            sec = 0
            cnt += k

        for i in customer:
            if i == 0:
                flag = 1
                break
            if i == c_sec:
                if cnt < 1:
                    flag = 1
                    break
                else:
                    cnt -= 1
        if flag:
            break
    if flag:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')