arr = [[1, 3], [0, 3], [1, 4], [1, 5], [0, 1], [2, 4]]
# 0번쨰 인덱스를 기준으로 정렬
sort1 = sorted(arr, key=lambda x: x[0])
print(sort1)
print()
# 0번쨰 인덱스 기준으로 정렬 후 1번째 인ㄷ게스 기준으로 정렬
sort2 = sorted(arr, key=lambda x: (x[0], x[1]))
print(sort2)
print()

# 빈도수가 가장 많은 문자를 출력해라.
# 단, 빈도수가 같다면 사전적으로 빠른 문자를 출력해라.
arr2 = ['A', 'B', 'Z', 'Z', 'A', 'Y', 'Y', 'Y', 'A', 'T']
sort3 = sorted(arr2, key=lambda x: (-arr.count(x), x))
print(sort3)