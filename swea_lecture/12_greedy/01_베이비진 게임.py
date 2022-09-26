def card_run(bucket):
    for i in range(10):
        if bucket[i] == 3:
            return True
    for i in range(8):
        if bucket[i] > 0 and bucket[i+1] > 0 and bucket[i+2] > 0:
            return True
    return False

t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    one = [0]*10
    two = [0]*10
    result = 0
    while arr:
        one[arr.pop(0)] += 1
        two[arr.pop(0)] += 1

        if card_run(one):
            result = 1
            break
        elif card_run(two):
            result = 2
            break
    print(f'#{tc} {result}')



# 3
# 9 9 5 6 5 6 1 1 4 2 2 1
# 5 3 2 9 1 5 2 0 9 2 0 0
# 2 8 7 7 0 2 2 2 5 4 0 3