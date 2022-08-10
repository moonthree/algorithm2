apart = [[15, 18, 17], [4, 6, 9], [10, 1, 3], [7, 8, 9], [15, 2, 6]]

family = list(map(int, input().split()))

def isPattern(y):
    for i in range(3):
        if apart[y][i] != family[i]:
            return 0
    return 1

for y in range(5):
    if isPattern(y):
        print(f'{5-y}층')
        break