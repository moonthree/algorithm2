# sorry friend
# used, path
# 제외시킬 친구 문자로 입력받기
# 그 친구를 제외한 모든 순열 출력

arr = ['E', 'W', 'A', 'B', 'C']

depth = 4
branch = len(arr)

path = ['']*depth
used = [0]*branch

n = input()

def sorry(level):
    if level == depth:
        for i in range(level):
            print(path[i], end='')
        print()
        return
    for i in range(branch):
        if arr[i] == n:
            continue
        if used[i] == 1:
            continue
        used[i] = 1
        path[level] = arr[i]
        sorry(level+1)
        used[i] = 0
sorry(0)