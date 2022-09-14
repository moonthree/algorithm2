def bs(array, target, st, ed):
    if st > ed:
        return None
    mid = (st + ed) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return bs(array, target, st, mid - 1)
    
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return bs(array, target, mid + 1, ed)

arr = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]
target = int(input())
result = bs(arr, target, 0, len(arr)-1)

if result == None:
    print('X')
else:
    print('O')