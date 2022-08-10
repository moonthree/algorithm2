train = [3, 7, 6, 4, 2, 9, 1, 7]
team = list(map(int, input().split()))

def isTeam(idx):
    for i in range(len(team)):
        if train[idx+i] != team[i]:
            return 0
    return 1

start = 0
for i in range(len(train)):
    result = isTeam(i)
    if result == 1:
        start = i
        break

print(f'{start}번~{start + len(team) - 1}번 칸')