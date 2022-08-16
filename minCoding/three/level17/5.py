arr = [[3, 5, 9], [4, 2, 1], [5, 1, 5]]

num_list = list(map(int, input().split()))

def isExist(nums):
    for i in nums:
        exist = False
        for j in range(len(arr)):
            for k in range(len(arr[j])):
                if i == arr[j][k]:
                    exist = True
        if exist:
            print(f'{i}:존재')
        else:
            print(f'{i}:미발견')
    return ''

print(isExist(num_list))