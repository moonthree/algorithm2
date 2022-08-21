number = [3, 6, 21, 4, 7]

tmp = number[0]

for i in number:
    if i > tmp:
        tmp = i
print(tmp)