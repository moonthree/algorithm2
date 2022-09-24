# 01
arr = ['A', 'B', 'Z', 'Z', 'A', 'Y', 'Y', 'Y', 'A', 'T']
sort6 = sorted(arr, key=lambda x: (-arr.count(x), x))
print(sort6)
# 01 -> ['A', 'A', 'A', 'Y', 'Y', 'Y', 'Z', 'Z', 'B', 'T']

# 02
arr2 = [2, 9, 9, 9, 3, 3, 3, 5, 5, 5, 7, 7]
sort7 = sorted(arr2, key=lambda x: (arr2.count(x), -x))
print(sort7)
# 02 -> [2, 7, 7, 9, 9, 9, 5, 5, 5, 3, 3, 3]