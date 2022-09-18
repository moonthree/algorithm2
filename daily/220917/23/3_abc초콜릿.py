arr = ['A', 'B', 'C']

n = int(input())
cnt = 0
path = []
def recur(level):
    global cnt
    if level == n:
        for i in range(len(path)-2):
            if path[i] == path[i+1] == path[i+2]:
                cnt -= 1
                break
        cnt += 1
        return
    for i in range(3):
        path.append(arr[i])
        recur(level+1)
        path.pop()

recur(0)
print(cnt)