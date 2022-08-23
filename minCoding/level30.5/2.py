arr = ['o', 'x']

n = int(input())
path = [0]*n
def recur(level):

    if level == n:
        for i in path:
            print(i, end='')
        print()
        return

    for i in range(2):
        path[level] = arr[i]
        recur(level+1)

recur(0)