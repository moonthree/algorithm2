def bs(array, st, ed):
    mid = (st + ed) // 2
    if st > ed:
        return mid
    elif array[mid] == '0':
        return bs(array, st, mid-1)
    elif array[mid] == '#':
        return bs(array, mid+1, ed)


n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input()))
arr2 = sum(arr, [])

result = bs(arr2, 0, len(arr2)-1)

y = result // n
x = result % n

print(y, x)