'''
5
8
C D 1
A B 9
A C 3
A E 7
B D 11
A D 20
B C 14
C E 5
'''
# def findboss(member):
#     global arr3
#     if arr3[ord(member)] == 0:           # 본인의 보스가 없으면 본인이 보스임
#         return member
#     ret = findboss(arr3[ord(member)])    # 배열에 적혀있는 값으로 다시 보스 찾아보기
#     return ret
#
# def union(a, b, idx):
#     global arr3
#     aboss = findboss(a)
#     bboss = findboss(b)
#     if aboss == bboss:
#         return 0
#     arr3[ord(bboss)] = aboss
#     return int(arr[idx][2])
#
# node = int(input())
# line = int(input())
#
# arr = [list(input().split()) for _ in range(line)]
# arr = sorted(arr, key=lambda x:int(x[2]))
# print(arr)
# arr3 = [0]*200
#
# cnt = 0
# i = 0
# ssum = 0
# while cnt != node-1:
#     ret = union(arr[i][0], arr[i][1], i)
#     i += 1
#     if ret != 0:
#         cnt += 1
#     ssum += ret
#
# print(ssum)

k = int(input())  # 정점개수
n = int(input())  # 간선개수
lst = [list(input().split()) for _ in range(n)]  # 간선의 정보 입력

lst.sort(key=lambda x: int(x[2]))

arr = [0] * 200


def findboss(member):
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret


def union(y, x, i):
    global answer, cnt
    yboss, xboss = findboss(y), findboss(x)
    if yboss == xboss:
        return
    answer += int(lst[i][2])  # 비용 더하기
    cnt += 1  # 간선의개수 더하기
    arr[ord(xboss)] = yboss


answer = 0  # 비용을 더할 변수
cnt = 0  # 간선의 개수를 더할 변수
for i in range(n):
    if cnt == k - 1:  # cnt가 간선의 개수 -1 개와 같으면
        print(answer)
        break
    union(lst[i][0], lst[i][1], i)

'''
5
8
C D 1
A B 9
A C 3
A E 7
B D 11
A D 20
B C 14
C E 5
'''