n = int(input())

arr = [0, 3, 1, 2, 1, 3, 2, 1, 2, 1, 99]

def jump(start):
    if arr[start] == 99:
        print('도착', end=' ')
        return
    print(arr[start], end=' ')
    jump(start+arr[start])
    print(arr[start], end=' ')

print('시작', end=' ')
jump(n)
print('시작')
