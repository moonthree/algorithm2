

tribe = [['A', 'B'], ['A', 'C'], ['D', 'E'], ['D', 'E'], ['D', 'F'],
         ['G', 'H'], ['I', 'J']]
mem = []
arr = [0]* 200
def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    return ret

def union(a, b):
    global arr
    mem.append(a)
    mem.append(b)
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return
    arr[ord(bboss)] = aboss

for i in range(len(tribe)):
    union(tribe[i][0], tribe[i][1])

n = int(input())
for i in range(n):
    y, x = input().split()
    union(y, x)

mem = set(mem)
mem = list(mem)
#print(mem)
cnt = 0
for i in mem:
    if findboss(i) == i:
        cnt += 1
print(f'{cnt}개')