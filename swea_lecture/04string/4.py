t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = input()

    if str2.find(str1) == -1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')