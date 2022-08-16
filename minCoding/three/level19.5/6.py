maps = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'A', 'C', 'D']]

pattern = [list(map(str, input())) for _ in range(2)]

flag = 0

def isPattern(a, b):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if maps[i+a][j+b] != pattern[i][j]:
                return 0
    return 1

for i in range(len(maps)):
    for j in range(0, len(maps[i])-1):
        result = isPattern(i, j)
        if result == 1:
            flag += 1
            
if flag:
    print(f'발견({flag}개)')
else:
    print('미발견')