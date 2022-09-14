arr = [0]*20
lst = [4, 2, 9, 7, 15, 1, 3]

def insert(target):
    now = 1
    while 1:
        if arr[now] == 0:
            arr[now] = target
            return
        if arr[now] < target:
            now = now * 2 + 1
        else:
            now = now * 2

def search(target):
    now = 1
    while 1:
        if now >= 20:      # 배열범위 벗어날 경우
            return 0
        if arr[now] == 0:       # 찾고자 하는 값이 없을경우
            return 0
        if arr[now] == target:  # 찾았을 경우
            return 1
        if arr[now] < target:
            now = now*2+1
        else:
            now = now*2


for i in range(len(lst)):
    insert(lst[i])              # arr배열(트리)에 값 저장하기

n = int(input())                # 숫자 하나 입력받고
answer = search(n)              # 입력받은 숫자가 존재하는지 search하는 함수
if answer:
    print('존재')
else:
    print('없는숫자')