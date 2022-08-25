def recur(idx):
    if idx == 5:
        print(f'{idx}번')
        return
    recur(idx + arr[idx])
    print(f'{idx}번')

arr = [3, 2, -1, 3, -2, 5, -1]

n = int(input())

recur(n)