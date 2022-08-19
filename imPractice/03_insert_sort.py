# 삽입 정렬 insert sort

a = [4, 7, 1, 3, 5, 2]

result = []
for i in range(len(a)):
    result.append(a[i])                     # 값 하나씩 내리기
    for j in range(i, 0, -1):               # 뒤에서 부터.. 앞으로 가면서
        if result[j-1] > result[j]:         # 현재 vs 앞의값 비교
            result[j], result[j-1] = result[j-1], result[j]
        else:
            break