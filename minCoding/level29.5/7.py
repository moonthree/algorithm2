idx, life = map(int, input().split())

arr = ['_']*5

flag = True

while flag:
    arr[idx] = life
    for i in arr:
        print(i, end='')
    print()
    arr[idx] = '_'
    idx += 1
    life -= 1
    if idx > 4:
        flag = False
        break
    if life == 0:
        flag = False
        break

for i in arr:
    print(i, end='')
print()