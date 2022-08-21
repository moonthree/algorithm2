words = input()

def func(n):
    print(len(words)-n, end=' ')

    if n == len(words)-1:
        return

    func(n+1)
    print(len(words)-n, end=' ')

func(0)