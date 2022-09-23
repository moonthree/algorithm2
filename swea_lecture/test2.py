arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
path = [0]*7
answer = []

def dfs(level,start):
    global answer
    Sum = 0
    if level == 7:
        for i in range(level):
            Sum += path[i]
        if Sum == 100:
            for i in range(len(path)):
                answer.append(path[i])
            return answer
        return

    for i in range(start,9):
        path[level]=arr[i]
        dfs(level+1,i+1)

dfs(0,0)
answer = sorted(answer)
for i in range(len(answer)):
    print(answer[i])