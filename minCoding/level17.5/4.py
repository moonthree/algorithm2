arr = [['G', 'K', 'T'], ['P', 'A', 'C']]

str1, str2 = input().split()

def isExist(a, b):
    cnt_a = 0
    cnt_b = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if a == arr[i][j]:
                cnt_a += 1
            if b == arr[i][j]:
                cnt_b += 1
    
    if cnt_a + cnt_b == 2:
        return '대발견'
    elif cnt_a + cnt_b == 1:
        return '중발견'
    else:
        return '소발견'

print(isExist(str1, str2))