# 어제함
# 중복순열(다뽑기)
# 순열(앞에서 한 번 뽑은 거 다시 안 뽑기, 금-은-동)
# 가지치기 (연속해서 2개 안봅기), (특정 시작 제외), (특정 문자 전부 제외)

# 오늘함 = 조합
# A B C D 달리기 시합(순열)
# 3명을 묶어서 하나의 그룹
# 나올 수 있는 그룹의 조합은 무엇무엇이 있을까요?

# 조합
arr = ['A', 'B', 'C', 'D']
path = ['']*3

def abc(level):
    if level == 3:
        for i in range(3):
            print(path[i], end='')
        print()
        return

    for i in range(4):
        #1 path[level-1] -> 그전 단계에서 타고 들어온 곳
        #2 arr[i] -> 앞으로 들어갈 가지
        #3 그전 들어온 가지 < 앞으로 들어갈 가지 (True)
        if level > 0 and path[level - 1] >= arr[i]:
            continue
        path[level] = arr[i]
        abc(level+1)

abc(0)
print()

def abcd(level, start):
    if level == 3:
        for i in range(3):
            print(path[i], end='')
        print()
        return

    for i in range(start, 4):
        path[level] = arr[i]
        abcd(level+1, i+1)

abcd(0, 0)
