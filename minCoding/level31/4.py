arr = [list(input()) for _ in range(5)]

word = ['M', 'O', 'P', 'A', 'M']

flag = 0
cnt = 0
for y in range(len(arr)):
    cnt = 0
    for x in range(len(arr[y])):
        if arr[y][x] == word[x]:
            cnt += 1
    if cnt == 5:
        flag = 1


if flag:
    print('yes')
else:
    print('no')