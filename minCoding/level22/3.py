arr = ['B', 'G', 'T', 'K']
lv = int(input())
path = [0]*lv

def tree(level):
    if level == lv:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(len(arr)):
        # if level == 0 and i == 1 or i == 2:
        #     continue
        path[level] = arr[i]
        tree(level+1)

tree(0)