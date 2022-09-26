# 24시간 최대한 많은 화물차가 화물을 싣고 내리면 최대 몇 대의 화물차가 이용ㅇ?

# 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시
# 앞 작업 종료와 동시에 다음 작업 시작

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr2 = sorted(arr, key=lambda x: x[1])
    cnt = 1
    now = arr2[0][1]
    for i in range(1, len(arr2)):
        if now <= arr2[i][0]:
            now = arr2[i][1]
            cnt += 1
    print(f'#{tc} {cnt}')



