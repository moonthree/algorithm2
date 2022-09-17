pw = ['Jason', 'Dr.tom', 'EXEXI', 'GK12P', 'POW']
word = input()
flag = 0
def recur(level):
    global flag
    if level == 5:
        return
    if pw[level] == word:
        flag = 1
    recur(level+1)
    
recur(0)

if flag:
    print('암호해제')
else:
    print('암호틀림')