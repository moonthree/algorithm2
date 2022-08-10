vect = ['M', 'I', 'N', 'C', 'O', 'D', 'I', 'N', 'G']

n = int(input())
n_list = list(map(str, input().split()))

for i in n_list:
    cnt = 0
    for j in vect:
        if i == j:
            cnt += 1
    if cnt:
        print('O', end='')
    else:
        print('X', end='')