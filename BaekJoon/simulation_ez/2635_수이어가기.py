n = int(input())

maxi = int(-21e8)
maxi_arr = []
for i in range(1, n+1):
    arr = [n, i]
    while True:
        num = arr[-2] - arr[-1]

        if num < 0:
            if len(arr) > maxi:
                maxi = len(arr)
                maxi_arr = arr
            break
        else:
            arr.append(num)


print(maxi)
print(*maxi_arr)