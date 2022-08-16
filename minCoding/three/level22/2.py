words = []
n = 2
result = ''
def word(level):
    words.append(input())
    global result
    if level == n:
        if words[n] == words[n-1] == words[n-2]:
            result = 'WOW'
        elif words[n] != words[n-1] == words[n-2] or words[n] == words[n-1] != words[n-2]:
            result = 'GOOD'
        elif words[n] != words[n-1] != words[n-2]:
            result = 'BAD'
        return
    word(level + 1)
word(0)
print(result)
