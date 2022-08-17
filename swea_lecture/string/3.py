import sys
sys.stdin = open("3_input.txt", "r")

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    arr = [input() for _ in range(n)]
    arr_new = []

    for i in range(n):
        for j in range(n - m + 1):
            arr_new.append(arr[i][j:m + j])
    for i in range(n):
        v_word = []
        for j in range(len(arr[i])):
            v_word.append(arr[j][i])
        result = ''.join(s for s in v_word)
        for k in range(len(result) - m + 1):
            arr_new.append(result[k:m + k])

    if m % 2 == 0:
        for i in range(len(arr_new)):
            if arr_new[i][:m//2] == arr_new[i][m: m//2-1: -1]:
                print(f'#{tc} {arr_new[i]}')
    else:
        for i in range(len(arr_new)):
            if arr_new[i][:m//2] == arr_new[i][m:m//2:-1]:
                print(f'#{tc} {arr_new[i]}')
