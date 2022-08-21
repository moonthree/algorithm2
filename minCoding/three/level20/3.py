arr = list(map(int, input().split()))

def abc(n):
    print(arr[n], end=' ')
    if n == len(arr)-1:
        return

    abc(n+1)
    print(arr[n], end=' ')

abc(0)