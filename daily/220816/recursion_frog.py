arr = [2, 0, 1, 1, 3, 5, 1]


def frog(level):
    if level >= len(arr):
        return
    frog(level + arr[level])
    print(arr[level], end=' ')


frog(0)
