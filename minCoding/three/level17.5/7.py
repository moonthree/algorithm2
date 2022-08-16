calorie_list = list(map(int, input().split()))

levelTable = [[10, 20], [30, 60], [100, 150], [200, 300]]

cnt = [0, 0, 0, 0]


for j in range(len(levelTable)):
    for i in calorie_list:
        if levelTable[j][0] <= i <= levelTable[j][1]:
            cnt[j] += 1

for i in range(len(cnt)):
    print(f'lev{i}:{cnt[i]}')