a, b = map(int, input().split())

def abc(a, b):
    print(a, end=' ')
    if a == b:
        return
    abc(a+1, b)
    print(a, end=' ')

abc(a, b)