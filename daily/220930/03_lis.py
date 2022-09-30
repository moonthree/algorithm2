arr = [10, 20, 10, 30, 20, 50]
result = [1] * len(arr)
for i in range(len(arr)):
    now = arr[i]
    for j in range(i):
        compare = arr[j]
        if now > compare:
            result[i] = max(result[j] + 1, result[i])
print(max(result))
