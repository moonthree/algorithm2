arr = ['a', 'b', 'c', 'd']
path = ['']*10

def abc(level):
    # 진입 후 리턴하는 경우
    if level > 0 and path[level-1]=='b':
        return 
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return
    for i in range(len(arr)):
        # 진입을 안하는 경우
        # if arr[i] == 'b':
        #     continue
        path[level] = arr[i]
        abc(level+1)

abc(0)