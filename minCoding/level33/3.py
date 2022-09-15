n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
arr2 = [0]*200
arr = [0]*200
def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    return ret


def union(a, b):
    global arr, cnt, arr2, flag
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        flag = 1
        return
    arr[ord(bboss)] = aboss

cnt = 0
ret = 0
flag = 0
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if y > x: continue
        if matrix[y][x] == 1:
            union(chr(y+65), chr(x+65))
# for i in arr2:
#     if i >= n:
#         flag = 1
#         break
if flag:
    print('cycle 발견')
else:
    print('미발견')