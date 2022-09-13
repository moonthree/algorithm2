t = int(input())
arr = [1, 2, 2]
for tc in range(1, t + 1):
    n = int(input())
    width = n // 10
    path = [0]*width
    cnt = 0
    def rect(level, wid):
        global cnt
        if wid == width:
            cnt += 1
            return
        for i in range(3):
            if sum(path) > width-1:
                break
            path[level] = arr[i]
            rect(level+1, wid+arr[i])
            path[level] = 0
    rect(0, 0)
    print(f'#{tc} {cnt}')