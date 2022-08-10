arr = ['A', 'T', 'K', 'P', 'T', 'C', 'A', 'B', 'C']
a, b = input().split()

a_idx = 0
b_idx = 0
for i in range(len(arr)):
    if arr[i] == a:
        a_idx = i
        break

for i in range(len(arr)-1, 0, -1):
    if arr[i] == b:
        b_idx = i
        break

print(b_idx-a_idx)