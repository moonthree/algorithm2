# 각 항에서 1~4 사이의 숫자를 1개씩 택해서 다
# 더했을떄 10이 나오는 경우는 몇가지 인가요?
# n 개의 항에서 1~4 사이의 숫자를 택할 것입니다.

arr = [1, 2, 3, 4]
n = int(input())
cnt = 0
def dfs(level, total):
    global cnt
    if level == n:
        if total == 10:
            cnt += 1
        return
    for i in range(4):
        dfs(level+1, total+arr[i])

dfs(0, 0)
print(cnt)