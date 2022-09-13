test_case = int(input())

for t in range(test_case):
    P, A, B = map(int, input().split())

    def binary_search(start, end, value):
        cnt = 0
        while(1):
            mid = int((start+end)/2)
            if mid == value:
                return cnt
            elif mid > value:
                end = mid
                cnt += 1
            elif mid < value:
                start = mid
                cnt += 1
            if start > end:
                return 0

    A_bs = binary_search(1, P, A)
    B_bs = binary_search(1, P, B)

    if A_bs < B_bs:
        print(f'#{t+1} A')
    elif A_bs > B_bs:
        print(f'#{t+1} B')
    else:
        print(f'#{t+1} 0')