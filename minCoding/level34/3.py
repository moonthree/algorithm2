def bs(array, target, st, ed):
    global cnt
    if st > ed:
        return None
    mid = (st + ed)//2

    if array[mid] == target:
        return target
    elif array[mid] > target:
        cnt += 1
        return bs(array, target, st, mid - 1)
    else:
        cnt += 1
        return bs(array, target, mid + 1, ed)


n = int(input())
arr = list(input().split())
arr.sort()
m = int(input())
for i in range(m):
    target, sec = input().split()
    cnt = 1
    result = bs(arr, target, 0, len(arr)-1)

    if int(sec) < cnt or result == None:
        print('fail')
    else:
        print('pass')