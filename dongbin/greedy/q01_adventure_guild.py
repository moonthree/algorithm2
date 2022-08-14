n = int(input())
arr = list(map(int, input().split()))
arr.sort()

group = 0       # 총 그룹의 수
cnt = 0         # 현재 그룹에 포함된 모험가의 수

for i in arr:       # 공포도가 낮은 모험가부터 하나씩 확인하며
    cnt += 1        # 현재 그룹에 모험가를 포함시키기
    if cnt >= i:    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group += 1  # 총 그룹의 수 증가시키기
        cnt = 0     # 현재 그룹에 포함된 모험가의 수 초기화

print(group)