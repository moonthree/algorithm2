#greedy 동전교환 문제

coin = [100, 50, 10]
change = int(input()) # 거슬러 줄 돈   250
answer = 0  # 총 동전 사용 개수

index = 0
while(1):
    cnt = change//coin[index]   # cnt=2
    change -= (cnt*coin[index]) # 나머지 거슬러 줘야 할 돈 50
    answer += cnt
    index += 1 # 그다음 50원 동전 사용을 하기 위해 index 1 증가
    if index == 3:
        break
print(answer)