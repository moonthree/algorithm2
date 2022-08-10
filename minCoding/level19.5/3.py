nums = list(map(int, input().split()))

arr = [[i+(4*j) for i in range(1, 5)]for j in range(4)]

cnt = 1
def pwCheck(y, x):
    for i in nums:
        if arr[y][x] == i:
            return cnt
    return 0

for y in range(len(arr)):
    for x in range(len(arr[y])):
        print(pwCheck(y, x), end=' ')
        if pwCheck(y, x):
            cnt += 1
    print()