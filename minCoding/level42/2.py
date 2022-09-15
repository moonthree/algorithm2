arr = list(map(int, input().split()))


depth = 5
branch = 5
path = [0]*depth
Max = -21e8
Min = 21e8
used = [0]*branch
def cal(abcd):
    return (abcd[0] * abcd[1]) - (abcd[2] * abcd[3]) + abcd[4]

def abc(level):
    global Min, Max, used
    if level == depth:
        ret = cal(path)
        if ret > Max:
            Max = ret
        if ret < Min:
            Min = ret
        return

    for i in range(branch):
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = arr[i]
        abc(level+1)
        path[level] = 0
        used[i] = 0

abc(0)
print(Max)
print(Min)