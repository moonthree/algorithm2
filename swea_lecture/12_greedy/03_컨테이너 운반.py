t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    used = [False]*len(truck)
    # n개의 컨테이너, m대의 트럭
    # 최대 무게

    weight.sort(reverse=True)
    truck.sort()
    loaded = 0
    for i in weight:
        for j in range(len(truck)):
            if i <= truck[j] and not used[j]:
                loaded += i
                used[j] = True
                break

    print(f'#{tc} {loaded}')
