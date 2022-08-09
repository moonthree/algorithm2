arr = ['MTKC']
spell = input()

def isExist(word):
    exist = False
    for i in arr[0]:
        if i == word:
            exist = True
    if exist:
        return '발견'
    else:
        return '미발견'

print(isExist(spell))