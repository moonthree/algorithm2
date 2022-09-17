def abc(level):
    #print(level, end='')
    if level==2:
        #print('#', end='')
        return
    #print('#', end='')
    for i in range(2):
        #print(level, end='')
        abc(level+1)
        # print(level, end='')
    #print(level, end='')


abc(0)