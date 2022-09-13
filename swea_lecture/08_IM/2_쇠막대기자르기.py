t = int(input())

for tc in range(1, t+1):
    arr = list(input())

    iron = 0
    cnt = 0
    i = 0
    while i < len(arr):
        if arr[i] == '(' and arr[i+1] == ')':
            cnt += iron
            i += 2
        elif arr[i] == '(':
            iron += 1
            i += 1
        else:
            cnt += 1
            iron -= 1
            i += 1
    print(f'#{tc} {cnt}')

    # 1 2 3 0 0 3 4 0 4 0 2 1 / 1 0 1
