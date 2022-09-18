arr = ['B', 'G', 'T', 'K']

n = int(input())
path = []
def recur(level):
    if level == n:
        for i in path:
            print(i, end='')
        print()
        return
    for i in range(4):
        # if (level == 0 and arr[i] == 'G') or (level == 0 and arr[i] == 'T'):
        #     continue
        path.append(arr[i])
        recur(level+1)
        path.pop()

recur(0)