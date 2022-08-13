n = int(input())
cnt = 0
def abc(n, cnt):
    if cnt == 4:
        return
    abc(n+2, cnt+1)
    print(n, end=' ')

abc(n, cnt)