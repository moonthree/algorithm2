stra = [input() for _ in range(4)]
long = len(stra[0])
short = len(stra[0])
l = 0
s = 0
def words(level):
    global long
    global short
    global l
    global s
    if len(stra[level]) > long:
        long = len(stra[level])
        l = level
    if len(stra[level]) < short:
        short = len(stra[level])
        s = level
    if level == 3:
        print(f'긴문장:{l}')
        print(f'짧은문장:{s}')
        return
    words(level+1)

words(0)