arr = [1, 3, 3, 3, 1, 1, 3]
n = len(arr)
arr1 = arr[0:(1+n)//2]
arr2 = arr[(1+n)//2: n]

print(arr1)
print(arr2)

# 1 3 3 3 1 1 3
# 1 3 3 3 // 1 1 3
# 1 3 // 1 3
# 1 1
# 1