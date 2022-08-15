TC = int(input()) # testcase의 개수
for T in range(1, TC+1):
    N, M = map(int, input().split()) # 정수의 개수 N # 구간의 개수 M
    arr = list(map(int, input().split()))

    def GetSum(location):
        total = 0
        for x in range(3):
            total += arr[location+x]
        return total

    Max = 0
    Min = 10000
    for i in range(N-M+1):
        ret = GetSum(i)
        if ret > Max:
            Max = ret
        if ret < Min:
            Min = ret

    result = Max - Min
    print(f'#{T} {result}')