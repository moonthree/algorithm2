power = [50, 40, 99, 5, 25, 6, 37]
ckeck = [0]*7
Min = 21e8
# 모든 선수 참여
# 중복 x

def dfs(start,level,sum):
    global Min, power
    against = 0
    for i in range(7):
        if ckeck[i] == 0:
            against += power[i]
    gap = abs(sum-against)
    Min = min(Min,gap)
    if level == 6:
        return
    for i in range(start, 7):
        ckeck[i] = 1
        dfs(i+1, level+1, sum+power[i])
        ckeck[i] = 0


dfs(0,0,0) # start, level, sum
print(Min)