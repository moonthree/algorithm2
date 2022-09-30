def lcstring(a, b):
    len_a = len(a)
    len_b = len(b)
    arr = [[0]*(len_b+1) for _ in range(len_a+1)]
    MAX = -21e8
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif a[i-1] == b[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
                MAX = max(MAX, arr[i][j])
            else:
                arr[i][j] = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


a = 'BABJYP'
b = 'ABCBJY'
lcstring(a, b)
