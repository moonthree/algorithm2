test_case = int(input())

for t in range(1, test_case+1):
    N = int(input())
    H = list(map(int, input().split()))

    distance = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if H[i] > H[j]:
                cnt += 1

        if cnt > distance:
            distance = cnt

    print(f'#{t} {distance}')