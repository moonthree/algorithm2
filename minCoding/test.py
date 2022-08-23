arr = ['a', 'b', 'c', 'd']
path = [''] * 3


def abc(level):
    if level == 3:
        for i in range(3):
            print(path[i], end='')
        print()
        return

    for i in range(4):
        # 1 path[level-1] -> 그전 단계에서 타고 들어온 곳
        # 2 arr[i] -> 앞으로 들어갈 가지
        # 3 그전 들어온 가지 < 앞으로 들어갈 가지  (True)
        if level > 0 and path[level - 1] >= arr[i]: continue
        path[level] = arr[i]
        abc(level + 1)


abc(0)
