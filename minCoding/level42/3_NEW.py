import copy
arr = ['BTS', 'SES', 'BS', 'CBS', 'SES']

word = input()
path = []
words2 = ''
MIN = 21e8
def dfs(level):
    global words2, MIN
    if len(words2) >= len(word):
        if words2 == word:
            MIN = min(MIN, level)
        return

    for i in range(5):
        backup = copy.deepcopy(words2)
        words2 += arr[i]
        dfs(level+1)
        words2 = copy.deepcopy(backup)

dfs(0)

print(MIN)