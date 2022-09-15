arr = [10, 40, 60]

n = int(input())

Min = 21e8

def abc(level, total):
    global Min
    if total >= n:
        if level < Min:
            Min = level
        return

    for i in range(3):
        abc(level+1, total + arr[i])

abc(0, 0)
print(Min)