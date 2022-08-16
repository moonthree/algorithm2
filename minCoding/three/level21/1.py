def abc(n):
    if n == 3:
        return
    abc(n+1)
    abc(n+1)
    abc(n+1)

abc(0)