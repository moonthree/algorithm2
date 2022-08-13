arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []

a = 0
b = 0
while a+b != 8:
    if a == 4:
        result.append(arr2[b])
        b += 1
    elif b == 4:
        result.append(arr1[a])
        a += 1
    elif arr1[a] > arr2[b] or a == 4:
        result.append(arr2[b])
        b += 1
    elif arr1[a] <= arr2[b] or b == 4:
        result.append(arr1[a])
        a += 1

for i in result:
    print(i, end=' ')