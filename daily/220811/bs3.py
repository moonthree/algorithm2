curser=[   # 6*10 size 리스트 (배열)
 '##########',
 '##########',
 '###_______',
 '__________',
 '__________',
 '__________',
]

# 워드작업 중 정전으로 인하여 컴퓨터가 강제로 종료가 되었습니다.
# 다시 전기가 들어어 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을때 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그래밍을 완성해 주세요.
# 시간복잡도 (On^2)보다 빨라야 합니다.

def bs1(st,ed):
    Max=-1
    while(1):
        mid=(st+ed)//2
        if curser[mid][0]=='_':
            ed=mid-1
        elif curser[mid][0]=='#':
            Max=mid
            st=mid+1
        if st>ed:
            break
    return Max+1

def bs2(st,ed,yy):
    Maxx = -1
    while (1):
        mid = (st + ed) // 2
        if curser[yy][mid] == '_':
            ed = mid - 1
        elif curser[yy][mid] == '#':
            Maxx = mid
            st = mid + 1
        if st > ed:
            break
    return Maxx + 1   # 인덴트 때문에 버그 !!

yaxis=bs1(0,5)
xaxis=bs2(0,9,yaxis-1)
print(yaxis-1,xaxis)