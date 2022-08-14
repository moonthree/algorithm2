# 선택 정렬
a = [4, 7, 1, 3, 5, 2]

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]     # swap

for i in range(len(a)):
    print(a[i], end=' ')