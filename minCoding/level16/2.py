arr = [['A', 'B', 'K', 'T'], ['K', 'F', 'C', 'F'], ['B', 'B', 'Q', 'Q'], ['T', 'P', 'Z', 'F']]
one_arr = []
for i in arr:
    for j in range(4):
        one_arr.append(i[j])

a, b = map(str, input().split())

cnt = 0
for i in one_arr:
    if a == i:
        cnt += 1
    if b == i:
        cnt += 1

print(cnt)