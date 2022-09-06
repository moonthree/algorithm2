T = int(input())

for tc in range(1, T+1):
    K, N, M = map( int, input().split())
    stations = [0]* (N+20) #버스정류장 위치표시
    station_numbers = list(map(int, input().split()))
    #station에 위치표시
    for i in range(M):
        stations[station_numbers[i]] = 1

    current_station = 0 #지금 버스가 있는 위치
    charge_times = 0 #충전횟수
    flag = 0
    for s in range(N+1):
        battery = K
        for t in range(K, 0, -1):
            if stations[current_station+t] == 1:
                current_station += t
                charge_times += 1
                break
            else:
                battery -= 1

            if current_station >= N-K:
                flag = 1
                break
            elif battery == 0:
                flag = 2
                break
        if flag:
            break

    if flag == 1:
        print(f'#{tc} {charge_times}')
    elif flag == 2:
        print(f'#{tc} 0')

