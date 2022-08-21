# 전기버스
test_case = int(input())

for t in range(test_case):
    K, N, M = map(int, input().split())
    recharge_list = list(map(int, input().split()))

    now = 0                 # 현재 위치
    recharge_cnt = 0        # 충전 횟수
    stop = 1                # flag 역할

    def bus_stop(bus):
        for j in recharge_list:                     # 최대 거리에서 1씩 내려가면서 충전소 탐색
            if bus == j:                            # 발견하면 리턴
                return j
        return 1                                    # 발견 못하면 리턴 1

    while stop == 1:
        cant_recharge = 0                           # 충전 실패 cnt

        if now+K >= N:                              # 현재위치 + 최대이동거리로 목표에 도착할 수 있으면
            stop = 0                                # stop = 0
            break                                   # 종료

        for i in range(now+K, now, -1):             # k는 최대 이동가능한 정류장 수, now는 현재 버스 위치
            if bus_stop(i) != 1:                    # 충전소 발견 시
                now = bus_stop(i)                   # 현재 위치 충전소로 변경
                recharge_cnt += 1                   # 충전횟수 + 1
                break                               # 충전 시 거기서 멈춰야하므로 break

            elif bus_stop(i) == 1:                  # 발견 실패 시
                cant_recharge += 1                  # 충전 실패 + 1
                                                    # 충전 실패시 더 가야하므로 break 없음
                
        if cant_recharge == K:                      # 충전실패횟수 == 최대이동거리면
            stop = 2                                # stop = 2 -> while문 종료
            break                                   # 배터리 부족시 종료

    if stop:
        print(f'#{t + 1} 0')
    else:
        print(f'#{t + 1} {recharge_cnt}')