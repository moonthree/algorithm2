import sys
sys.stdin = open("3_input.txt", "r")

t = int(input())

for tc in range(1, t+1):

    n, m = map(int, input().split())

    arr = [list(input())for _ in range(n)]

    for i in range(n):
        for j in range(n-m+1):
            temp = []
            result = []
            for k in range(m):
                temp.append(arr[i][j+k])
            result.append(temp[::-1])
            if result[0] == temp:
                print(f'#{tc}', end=' ')
                print(''.join(result[0]))

    for i in range(n):
        for j in range(n-m+1):
            temp = []
            result = []
            for k in range(m):
                temp.append(arr[j+k][i])
            result.append(temp[::-1])
            if result[0] == temp:
                print(f'#{tc}', end=' ')
                print(''.join(result[0]))
