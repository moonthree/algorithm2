arr = list(map(int, input().split()))


flag = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            flag += 1

if flag:
    print('도플갱어 발견')
else:
    print('미발견')