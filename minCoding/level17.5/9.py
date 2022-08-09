arr = list(map(int, input().split()))

masking = [1, 0, 1, 0, 1, 0]

for i in range(len(arr)):
    if masking[i] == 0:
        arr[i] = 0

tmp_min = arr[0]
tmp_idx = 0
for i in range(0, len(arr)-2, 2):
    if arr[i] < arr[0]:
        tmp_min = arr[i]
        tmp_idx = i
print(f'arr[{tmp_idx}]={tmp_min}')