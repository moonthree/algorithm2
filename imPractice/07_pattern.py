arr = [3, 6, 5, 8, 5, 3, 5, 8, 5, 3, 3, 1, 1, 3]
pattern = [3, 5, 8, 4]
flag = 0
def isPattern(index):
    for i in range(4):
        if arr[index+i] != pattern[i]:
            return 0
    return 1

for i in range(11):   # 0 ~ 10
    ret = isPattern(i)
    if ret == 1:
        flag = 1
        break

if flag:
    print("패턴존재")
else:
    print('패턴은 존재하지 않음')