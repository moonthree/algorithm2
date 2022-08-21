arr = [[3, 2, 4, 1],
       [0, 1, 0, 5],
       [2, 0, 3, 0],
       [5, 4, 0, 2],
       [2, -5, 0, 3]]

Max = int(-21e8)


def dfs(now, level, sum):
    global Max
    if level == 5:
        if sum > Max:
            Max = sum
        return
    for i in range(3):
        direct = [-1, 0, 1]
        dy = level
        dx = now + direct[i]
        if dx < 0 or dx > 3: continue  # 맵 범위
        if arr[dy][dx] == 0: continue  # 벽이면 노놉
        dfs(dx, level + 1, sum + arr[dy][dx])


dfs(0, 0, 0)  # now level sum
print(Max)
