t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    pizza = []              # 굽고 있는 피자
    pizza_idx = []          # 굽고 있는 피자의 idx
    arr_idx = n             # 추가할 피자의 idx
    
    for i in range(n):      # 처음에 화덕 크기만큼 피자 넣기
        pizza.append(arr.pop(0))
        pizza_idx.append(i)

    idx = 0                         # 현재 꺼낼 위치의 화덕 idx
    while len(pizza) > 1:           # 화덕에 피자 1개 남을때 까지
        if idx >= len(pizza):       # 한 바퀴 돌면 화덕 idx 초기화
            idx = 0

        pizza[idx] = pizza[idx] // 2    # 치즈 반절로 - 치즈 반절이 치즈0 체크보다 위에 있어야함

        if pizza[idx] == 0:             # 치즈 0이면
            pizza.pop(idx)              # 해당 피자 꺼내기
            pizza_idx.pop(idx)          # 해당 피자의 idx도 꺼내기
            
            if len(arr) > 0:                        # 굽지 않은 피자가 남아있으면
                pizza.insert(idx, arr.pop(0))       # 피자 꺼낸 자리(idx)에 피자 넣기
                pizza_idx.insert(idx, arr_idx)      # 피자 꺼내 자리에 추가한 피자의 idx도 넣기
                arr_idx += 1                        # 대기중인 5번피자 넣었으면 6번피자 대기중이니까 += 1

        idx += 1    # 화덕 idx

    print(f'#{tc} {pizza_idx[0]+1}')


