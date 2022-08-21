n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr_find = list(map(int, input().split()))

arr.sort()

def binary_search(st, ed, target):
    while (1):
        mid = (st + ed)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            ed = mid - 1
        elif arr[mid] < target:
            st = mid + 1
        if st > ed:
            return 0

for i in arr_find:
    result = binary_search(0, n-1, i)
    if result:
        print(1)
    else:
        print(0)


# n = 5
# arr = [4, 1, 5, 2, 3]
# m = 5
# arr_find = [1, 3, 7, 9, 5]
# arr.sort() -> arr = [1, 2, 3, 4, 5]

# for i in arr_find:  1, 3, 7, 9, 5
# i = 1 ###################################
# result = binary_search(0, n-1, 1)  -> st = 0, ed = n-1, target = 1  -> n이 5면 arr의 마지막 크기는 4이므로 ed = n-1

# def binary_search(0, 4, 1)
# while(1):
# mid = (0 + 4)//2 -> mid = 2
# arr[2] = 3, target = 1
# -> arr[2] > target
# -> ed = mid - 1
# -> ed = 2 - 1
# -> ed = 1

# mid = (0 + 1)//2 -> mid = 0
# arr[0] = 1, target = 1
# -> arr[0] == target
# -> return 1
# result = 1 -> print(1)

# i = 3 ###################################
# def binary_search(0, 4, 3)
# while(1):
# mid = (0 + 4)//2 -> mid = 2
# arr[2] = 3, target = 3
# -> arr[2] == target
# -> return 1
# result = 1 -> print(1)

# i = 7 ###################################
# def binary_search(0, 4, 7)
# while(1):
# mid = (0 + 4)//2 -> mid = 2
# arr[2] = 3, target = 7
# -> arr[2] < target
# -> st = mid + 1
# -> st = 2 + 1 = 3

# mid = (3 + 4)//2 -> mid = 3
# arr[3] = 4, target = 7
# -> arr[3] < target
# -> st = mid + 1
# -> st = 3 + 1 = 4

# mid = (4 + 4)//2 -> mid = 4
# arr[4] = 4, target = 7
# -> arr[4] < target
# -> st = mid + 1
# -> st = 4 + 1 = 5

# if st > ed:
# -> return 0
# result = 0 -> print(0)