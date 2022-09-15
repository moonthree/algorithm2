nation = int(input())
arr_p = [0]*200
population = list(map(int, input().split()))
for i in range(len(population)):
    arr_p[i+65] += population[i]

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
    arr[ord(bboss)] = aboss

n = int(input())

for i in range(n):
    a, b, c = input().split()
    if a == 'alliance':
        union(b, c)
    elif a == 'war':
        b_boss = findboss(b)
        b_num = 0
        b_cnt = 0
        c_boss = findboss(c)
        c_num = 0
        c_cnt = 0
        for j in range(len(arr_p)):
            if arr_p[j] != 0:
                if findboss(chr(j)) == b_boss:
                    b_cnt += 1
                    b_num += arr_p[j]
                elif findboss(chr(j)) == c_boss:
                    c_cnt += 1
                    c_num += arr_p[j]
        if b_num > c_num:
            print(nation - c_cnt)
        else:
            print(nation - b_cnt)



