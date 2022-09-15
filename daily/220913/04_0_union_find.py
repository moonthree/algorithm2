# union find 자료구조
# 각각의 독립된 data를 그룹화 시킬 때 사용

arr = [0]*200
def findboss(member):
    global arr
    if arr[ord(member)] == 0:           # 본인의 보스가 없으면 본인이 보스임
        return member
    ret = findboss(arr[ord(member)])    # 배열에 적혀있는 값으로 다시 보스 찾아보기
    return ret


def union(a, b):
    global arr
    aboss = findboss(a)         # boss 찾기
    bboss = findboss(b)
    if aboss == bboss:          # boss가 같다 -> 이미 같은 그룹
        return
    arr[ord(bboss)] = aboss     # 두 보스가 다르다면 b의 보스에 해당하는 값에 a의 보스 적기


union('A', 'B')
union('D', 'E')
union('B', 'E')
union('B', 'D')
union('F', 'E')


y, x = input().split()
if findboss(y) == findboss(x):
    print('같은 그룹')
else:
    print('다른 그룹')