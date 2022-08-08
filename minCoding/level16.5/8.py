arr = [['A79TKQ'], ['MINCOD']]

a, b = input().split()

def isExist(word):
    exist = False
    for i in arr:
        if i[0].find(word) != -1:
            exist = True
    if exist:
        return '존재'
    else:
        return '없음'

print(f'{a} : {isExist(a)}')
print(f'{b} : {isExist(b)}')
