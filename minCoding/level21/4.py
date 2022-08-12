n = int(input())

def func(level):
    print(level, end='')
    if level == n:
        return
    for _ in range(2):
        func(level + 1)

func(0)