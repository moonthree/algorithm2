t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        a = arr.pop(0)
        arr.append(a)
        
    print(f'#{tc} {arr[0]}')


