n = int(input())

arr = [input() for _ in range(n)]

for i in range(len(arr)):
    if arr[i].islower():
        arr[i] = arr[i][0].upper() + arr[i][1:len(arr[i])]
    elif arr[i][0].isupper() == True and arr[i][1:len(arr[i])].islower() == True:
        continue
    else:
        arr[i] = arr[i].upper()

arr.sort()
for i in arr:
    print(i)