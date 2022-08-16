arr = list(map(int, input().split()))

for i in range(4):
    print(*arr[:4], end=' ')
    for j in range(i):
        print(arr[4+j], end=' ')
    print()