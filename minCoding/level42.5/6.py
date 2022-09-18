import copy
word = list(input())
n = int(input())
score= 0
MAX = -21e8
def dfs(level, start):
    global word, score, MAX
    temp = copy.deepcopy(word)
    if level == n:
        #print(word)
        score = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                score -= 50
            elif abs(ord(word[i]) - ord(word[i+1])) <= 5:
                score += 3
            elif abs(ord(word[i]) - ord(word[i+1])) >= 20:
                score += 10
        MAX = max(score, MAX)
        return

    for i in range(start, len(word)-1):
        for j in range(i, len(word)):
            word[i], word[j] = word[j], word[i]
            dfs(level+1, i+1)
            word = copy.deepcopy(temp)

dfs(0, 0)
print(MAX)