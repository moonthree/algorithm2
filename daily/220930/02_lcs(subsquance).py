def lcsubquence(a, b):
    len_a = len(a)
    leb_b = len(b)
    arr = [[0]*(leb_b+1) for _ in range(len_a+1)]
    for i in range(len_a+1):
        for j in range(leb_b+1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

    print(arr[len_a][leb_b])


a = 'BABJYP'
b = 'ABPABY'
lcsubquence(a, b)