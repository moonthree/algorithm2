arr = ['a', 'b', 'c', 'd']
path = ['']*10
used = [0]*10
def abc(level):
    # 진입 후 return
    if level > 1 and path[level-1] == path[level-2]:
        return
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(len(arr)):
        # 진입을 아예 안하는 경우
        # if level > 0 and (path[level-1]==arr[i]):
        #     continue
        path[level] = arr[i]
        abc(level+1)
        

abc(0)