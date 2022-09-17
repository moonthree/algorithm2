n = int(input())

path = []
def recur(level):
    if level == 4:
        for i in path:
            print(i, end='')
        print()
        return
    for i in range(1, n+1):
        path.append(i)
        recur(level+1)
        path.pop()


recur(0)