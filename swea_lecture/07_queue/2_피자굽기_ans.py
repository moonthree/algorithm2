t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    pizza = []  # 인덱스랑 피자 같이 담기
    for i in range(m):
        pizza.append([i + 1, arr[i]])  # 전부 담기, 나중에 출력 편하게 인덱스는 i+1로 담기
    
    oven = pizza[:n]    # 오븐 크기만큼 들어감
    wait = pizza[n:]    # 대기
    
    while len(oven) > 1:            # 오븐에 피자 1개 남을때 까지 반복

        check = oven.pop(0)         # 피자 꺼내서 확인
        check[1] = check[1]//2      # 피자 꺼내서 치즈 반절로 // [0]은 idx, [1]은 피자

        if check[1] == 0:                   # 치즈 0이면
            if wait:                        # 대기중인 피자가 있으면
                oven.append(wait.pop(0))    # 대기중인 피자 오븐에 넣기
        else:                               # 치즈가 0이 아니면
            oven.append(check)              # 오븐에서 꺼낸 피자 다시 오븐에 넣기

    print(f'#{tc} {oven[0][0]}')            # 오븐에 남아있는 피자의 idx 출력
