board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "T", "T"]
]

ptn = [list(input()) for _ in range(2)]

def findptn(dy, dx):
    for i in range(2):
        for j in range(2):
            if board[dy+i][dx+j] != ptn[i][j]:
                return 0
    return 1

cnt = 0
for y in range(2):
    for x in range(3):
        if findptn(y, x):    #0,0 ~~ 1,2
            cnt += 1
if not cnt:
    print("미발견")
else:
    print("발견")