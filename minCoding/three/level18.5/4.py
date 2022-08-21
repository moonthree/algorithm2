hippo = [list(map(int, input().split())) for _ in range(2)]

teeth = [0]*len(hippo[0])
for i in range(len(hippo)):
    for j in range(len(hippo[i])):
        if hippo[i][j] == 1:
            teeth[j] += 1

cnt = 0
for i in teeth:
    if i == 2:
        cnt += 1

print(f'{cnt}개')