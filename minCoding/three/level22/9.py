arr = ['Jason', 'Dr.tom', 'EXEXI', 'GK12P', 'POW']
password = input()

def pw(level):
    global password
    if level == 4:
        cnt = 0
        for i in arr:
            if password == i:
                cnt += 1
        if cnt:
            print('암호해제')
        else:
            print('암호틀림')
        return
    pw(level+1)

pw(0)