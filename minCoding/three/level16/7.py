word_list = [input() for _ in range(3)]

M = False
for i in word_list:
    for j in i:
        if j == 'M':
            M = True

if M:
    print('M이 존재합니다')
else:
    print('M이 존재하지 않습니다')