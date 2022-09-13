# k = 이동할 수 있는 정류장 수
# n = 종점
# m = 정류장 수
# bus_stop = 정류장 위치 리스트

t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    bus_stop = list(map(int, input().split()))

    flag = 1
    recharge_cnt = 0
    now = 0
    while flag == 1:
        if now+k >= n:
            flag = 2
            break

        move = 0
        for i in range(now+k, now, -1):
            recharge = 0
            for stop in bus_stop:
                if stop == i:
                    recharge = 1
                    recharge_cnt += 1
                    now = stop
                    break
            move += 1
            if recharge:
                break
        if move == k:
            flag = 0
            break

    if flag:
        print(recharge_cnt)
    else:
        print(0)


# 3
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17