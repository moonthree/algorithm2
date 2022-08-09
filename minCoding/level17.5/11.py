arr = [3, 5, 4, 2]

bit_arr = list(map(int, input().split()))

sums = 0
for i in range(len(bit_arr)):
    if bit_arr[i] == 1:
        sums += arr[i]

print(sums)