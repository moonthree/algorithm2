# 문자 하나를 입력 받아 주세요.
# 입력받은 문자의 형제 출력해주세요

# 1. 부모 찾아 출력하기
# 2. 형제 찾아 출력하기

ar = [[0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

ch = input()
idx = ord(ch)-65
answer = []

for i in range(6):
    if ar[i][idx] == 1:
        answer.append(i)

if len(answer) == 0:
    print("형제없음")
else:
    result = []
    for x in answer:
        for i in range(6):
            if ar[x][i] == 1:
                result.append(i)
    result.remove(idx)
    if len(result) == 0:
        print("형제없음")
    else:
        for x in result:
            print(chr(x+65))