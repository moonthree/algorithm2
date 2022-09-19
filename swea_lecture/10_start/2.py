t = int(input())

for tc in range(1, t+1):
    hexadecimal = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    leng, hex_num = input().split()
    result = ''
    for i in hex_num:
        if '0' <= i <= '9':
            temp = int(i)
        else:
            temp = hexadecimal[i]
        num = 8
        for _ in range(4):
            if temp & num:
                result += '1'
            else:
                result += '0'
            num >>= 1

    print(f'#{tc} {result}')
