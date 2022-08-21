
# 1은 가위, 2는 바위, 3은 보
# 1 > 3
# 3 > 2
# 2 > 1

# 진쪽을 리턴
def rcp(a, b):
    if a == b:
        return b
    elif a == 1 and b == 3:
        return b
    elif a == 1 and b == 2:
        return a
    elif a == 2 and b == 3:
        return a
    elif a == 2 and b == 1:
        return b
    elif a == 3 and b == 1:
        return a
    elif a == 3 and b == 2:
        return b

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    bucket = [1]*n
    flag = 1
    while flag:
        for_flag = 1
        for i in range(n):
            for j in range(i, n):
                if bucket[i] == 1 and bucket[j] == 1:
                    bucket[rcp(i, j)] = 0
                    for_flag = 0
                    break
            if not for_flag:
                break
        if sum(bucket) == 1:
            flag = 0

    print(bucket)