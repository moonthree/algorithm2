n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

medal = []

for i in arr:
    if len(medal) > 0:
        idx = 0
        for j in range(len(medal)):
            if int(i[1]) < int(medal[j][1]):
                idx += 1
        medal.insert(idx, i)
    else:
        medal.append(i)
    for k in range(len(medal)):
        if k > 2:
            break
        print(medal[k][0], end=' ')
    print()
