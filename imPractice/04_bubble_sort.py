# bubble 정렬

a = [8, 3, 12, 10, 1]

for i in range(len(a)-1, 0, -1):  # 4 3 2 1
    for j in range(0, i): # i가 4일때 0123  i가 3일때 012...
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
