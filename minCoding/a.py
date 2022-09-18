arr = [i for i in range(1, 257)]
n = int(input())
for i in range(n**3):
    res = []
    for j in range(0, n**4, n**3):
        res.append(arr[i+j])
    print(res)
