sen = list(input())
t1, t2 = input().split()

for i in range(len(sen)): #5일때 0,1,2,3,4
    if t1 or t2 == sen[i]:
        if i-1 < 0 or i+1 > 4:
            continue
        sen[i - 1] = '#'
        sen[i + 1] = '#'

print(sen)