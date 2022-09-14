def bs(array, st, ed):
    mid = (st + ed) // 2
    if mid == 9:
        if array[mid] == '#':
            return mid
    if array[mid] == '#' and array[mid+1] == '_':
        return mid
    elif array[mid] == '_':
        return bs(array, st, mid - 1)
    elif array[mid] == '#':
        return bs(array, mid+1, ed)


arr = list(input())

result = bs(arr, 0, len(arr)-1)

print(f'{(result+1)*10}%')