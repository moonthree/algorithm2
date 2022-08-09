number = [21, 6, 21, 4, 7]

tmp = number[0]

for i in number:
    if i > tmp:
        tmp = i

cnt = 0
for i in number:
    if tmp == i:
        cnt += 1
print(cnt)