n = int(input())

def countdown(num):
    print(num, end=' ')
    if num == 0:
        return

    countdown(num-1)
    print(num, end=' ')

countdown(n)