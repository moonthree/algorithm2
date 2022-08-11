test_case = int(input())


for t in range(test_case):
    K, N, M = map(int, input().split())
    recharge_list = list(map(int, input().split()))

    now = 0
    recharge_cnt = 0
    stop = 1

    def bus_stop(bus):
        for j in recharge_list:
            if bus == j:
                return j
        return 1

    while stop == 1:
        if now+K >= N:
            stop = 0
            break
        isStop = 0
        for i in range(now+K, now, -1):
            if bus_stop(i) != 1:
                now = bus_stop(i)
                recharge_cnt += 1
                break
            elif bus_stop(i) == 1:
                isStop += 1
        if isStop == K:
            stop = 2
            break

    if stop:
        print(f'#{t + 1} 0')
    else:
        print(f'#{t + 1} {recharge_cnt}')