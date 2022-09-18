word = input()

path = []
cnt = 0
def recur(level):
    global cnt
    if level == 4:
        for i in range(3):
            if (path[i] == 'B' and path[i+1] == 'T') or (path[i] == 'T' and path[i+1] == 'B'):
                cnt -= 1
                break
        cnt += 1
        return

    for i in range(4):
        path.append(word[i])
        recur(level+1)
        path.pop()

recur(0)
print(cnt)