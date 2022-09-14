def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

def union(a, b):
    global arr
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return 1
    arr[ord(bboss)] = aboss


n=int(input())
edge=[]
for _ in range(n):
    edge.append(input().split())

arr=[0]*200

# union 함수

answer = '미발견'
for i in range(n):
    aa, bb=edge[i]
    ret = union(aa, bb)
    if ret==1:
        answer = '발견'
        break
print(answer)