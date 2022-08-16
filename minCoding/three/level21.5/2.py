arr = [[3, 4, 1, 5], [3, 4, 1, 3], [5, 2, 3, 6]]

Sum = [0]*4

for y in range(len(arr)):
    for x in range(len(arr[y])):
        Sum[x] += arr[y][x]

index = int(input())

print(Sum[index])