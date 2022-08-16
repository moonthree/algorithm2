def abc(level):
    #print('#', end='')
    if level==2:
        #print('#', end='')
        return
    #print('#', end='')
    for i in range(2):
        #print('#', end='')
        abc(level+1)
        #print('#', end='')
    #print('#', end='')


abc(0)