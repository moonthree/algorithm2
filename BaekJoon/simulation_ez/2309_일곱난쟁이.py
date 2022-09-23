arr = []
for _ in range(9):
    arr.append(int(input()))

path = []
def recur(level, total, start):
    if level == 7:
        if total == 100:
            path.sort()
            for i in path:
                print(i)
            quit()
    for i in range(start, 9):
        path.append(arr[i])
        recur(level+1, total+arr[i], i+1)
        path.pop()

recur(0, 0, 0)