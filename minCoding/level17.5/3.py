name1 = input()
name2 = input()

def isSame(a, b):
    if a == b:
        return 0
    else:
        return 1

same = isSame(name1, name2)

if same == 0:
    print('동명')
else:
    print('남남')