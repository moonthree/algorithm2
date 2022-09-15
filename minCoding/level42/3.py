import copy

text = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
target = input()
MIN = 21e8

def dfs(level, result, cnt):
    global MIN, target
    if len(result) >= len(target):
        if result == target:
            if MIN > cnt:
                MIN = cnt
        return
    for i in range(5):
        backup = copy.deepcopy(result)
        result += text[i]
        dfs(level+1, result, cnt+1)
        result = copy.deepcopy(backup)

dfs(0, '', 0)
print(MIN)