arr = [1, 2]
n = int(input())

for i in range(n-1):
    arr.append(arr[i] + arr[i+1])
print(arr[n-1])