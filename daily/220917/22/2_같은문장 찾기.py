word = []

def dfs(level):
    a = input()
    word.append(a)

    if level == 2:
        if word[level] == word[level-1] == word[level-2]:
            print('good')
        return