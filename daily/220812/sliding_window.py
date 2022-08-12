arr = [4, 7, 1, 8, 9, 3, 5, 8, 6, 6, 9]

MAX = int(-21e8)

for i in range(len(arr)-4):
    sums = 0
    for j in range(i, i+5):
        sums += arr[j]
    if MAX < sums:
        MAX = sums

print(sums)