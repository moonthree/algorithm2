words = input()

ghost = 'GHOST'

flag = 0

def isPattern(idx):
    for i in range(len(ghost)):
        if words[i+idx] != ghost[i]:
            return 0
    return 1

for i in range(len(words)):
    result = isPattern(i)
    if result == 1:
        flag = 1
        break

if flag:
    print('존재')
else:
    print('존재하지 않음')