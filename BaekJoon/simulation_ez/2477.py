n = int(input())
arr = []
for _ in range(6):
    a, b = map(int, input().split())
    arr.append([a, b])

bucket = [0]*6
small = 0
garo = 0
sero = 0
for i in range(len(arr)):
    bucket[arr[i][0]] += 1
    if arr[i][0] == 4 or arr[i][0] == 2:
        if bucket[arr[i][0]] == 2:
            small = arr[i][1] * arr[i+1][1]
            break
    else:
        if bucket[arr[i][0]] == 2:
            small = arr[i][1] * arr[i-1][1]
            break
for i in range(len(arr)):
    if arr[i][0] == 4:
        sero += arr[i][1]
    elif arr[i][0] == 2:
        garo += arr[i][1]

print((garo*sero-small)*n)