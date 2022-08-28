t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    distance = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):     # 빈 칸 포함 전부 탐색시 낙차 파악 가능
            if arr[i] > arr[j]:
                cnt += 1
        if distance < cnt:
            distance = cnt

    print(f'#{tc} {distance}')
