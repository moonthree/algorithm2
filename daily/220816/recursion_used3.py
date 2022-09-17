depth = 3
arr = ['a', 'b', 'c', 'd']

path = ['']*10
used = [0]*4

def abc(level):
    # 진입하고 리턴함
    # if level == 1 and path[level-1] == 'c':
    #     return

    if level == depth:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(4):
        # 아예 진입을 안함
        if level == 0 and arr[i] == 'c':
            continue
        path[level] = arr[i]
        abc(level+1)

abc(0)