t = int(input())
for tc in range(1, t+1):
    num = float(input())
    ret = ''
    two = 1
    for _ in range(12):
        two *= 0.5
        if num - two >= 0:
            ret += '1'
            num -= two
            if not num:
                break
        else:
            ret += '0'

    if num:
        ret = 'overflow'
    print(f'#{tc} {ret}')
