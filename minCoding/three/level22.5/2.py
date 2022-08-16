# wow

n = int(input())
arr = ['x', 'o']
path = ['']*n

def wind(level):
    if level == n:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(len(arr)):
        path[level] = arr[i]
        wind(level + 1)

wind(0)