word = list(input())

st = ord('A')
ed = ord('Z')+1

vert = ord(max(word)) - st + 2

arr = [['_']*len(word) for _ in range(vert)]

for y in range(vert):
    for x in range(len(word)):
        if ord(word[x]) - y < st:
            continue
        arr[y][x] = chr(ord(word[x]) - y)

for y in range(vert):
    for x in range(len(word)):
        print(arr[y][x], end='')
    print()