T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    distance = 0
    for i in range(len(arr)):
        cnt = 0
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1

        if distance < cnt:
            distance = cnt

print(tc, distance)